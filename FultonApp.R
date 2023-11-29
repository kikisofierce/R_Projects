#Author: Jahru McCulley
#Project:Automate Apartment Add Posting to Facebook 
###########
library(rvest)
library(RSelenium)
library(tidyverse)
library(netstat)
library(lubridate)
library(stringr)
library(stringi)
library(httr)
library(getPass)
library(Rfacebook)
library(rlist)
library(jpeg)
library(magick)
library(seleniumPipes)
library(readxl)
library(shiny)
library(shinyWidgets)
########################
system("docker start 8598164f201230fdb9abca60c40fab4a5e0a296fe6a8cddcbe2728502be5e92a")
###########################

ui <- fluidPage(
  
  titlePanel("FultonGrace Ad Posting Automator"),
  actionButton("Phase_0", "Open Excel File!"),
  actionButton("Phase_1", "Scrape FultonGrace.com!"),
  actionButton("Phase_3", "View Apartment Photos"), 
  actionButton("Phase_2", "Post to Facebook!"),
  sidebarLayout(
    sidebarPanel(
      strong("Step 1: Click Open Excel File! button."),
      p("(a) In the first column, paste the URL from Fultongrace.com"),
      p("(b) In the second column, paste the text you want to be included in the description."),
      p("(c) Save and close the excel file"),
      strong("Step 2: Click the Scrape FultonGrace.com! button"),
      strong("Step 3: Click the View Apartment Photos button"),
      p("(a) Wait for the pictures to appear in the folder. You can find the IMG folder on the Desktop"),
      p("(b) Make sure that there are only 10 photos in the IMG Folder BEFORE you move to Step 4"),
      p("(c) If you want to add more photos, put the other photos in a separate folder to add later to Facebook."),
      p("(d) Notice when the blue task bar is fully filled before proceeding to Step 4"),
      strong("Step 4: Click the Post to Facebook! button"),
      p("(a) When promoted, enter the authentication code , and click through until you reach homepage"),
      p("(b) click submit code"),
      p("(c) click submit until you get the to the homepage")

    ),
    mainPanel(
      img(src = "fulton.jpg", height = 140, width = 400), 
      img(src = "facebook.png", height = 140, width = 400)
      
    )))


  

server <- function(input, output, session) {
  observeEvent(input$Phase_0, {
    file.show("C:/Users/Open/Documents/FultonGrace/FultonGrace/Phase1/Fulton_urls.xlsx")
  })
  
  observeEvent(input$Phase_3, {
    opendir <- function(dir = "C:/Users/Open/Documents/FultonGrace/FultonGrace/IMG"){
      if (.Platform['OS.type'] == "windows"){
        shell.exec(dir)
      } else {
        system(paste(Sys.getenv("R_BROWSER"), dir))
      }
    }
    opendir() #file.show("C:/Users/Open/Documents/FultonGrace/FultonGrace/IMG")
  
    })
    
  N <- 1
observeEvent(input$Phase_1, {  
  withProgress(message = 'Calculation in progress', {
    for(i in 1:N){
      ################################################
      #run to ensure R messages are printed in English
      Sys.setenv("LANG" = "en")
      
      #set wd 
      setwd("C:/Users/Open/Documents/FultonGrace/FultonGrace/IMG")
      
      # Customized function to check class() and typeof() at once:
      check_object <- function(object) {
        cat("\nclass: ",
            class(object),
            "\ntypeof: ",
            typeof(object),
            "\n")
      }
      Sys.sleep(5)
      remDr <- remoteDriver(remoteServerAddr = "localhost",
                            port=4445L, 
                            browserName="firefox")
      remDr$open()
      
      ###########################################
      
      #upload URLs
      input_data <- read_excel("C:/Users/Open/Documents/FultonGrace/FultonGrace/Phase1/Fulton_urls.xlsx")
      
      url_data <- input_data$url
      raw_text <- (input_data$des) 
      
      raw_text <- str_replace_all(raw_text, "\r\n","")
      raw_text <- str_replace_all(raw_text, "\r\n\r\n","")
      raw_text <- str_replace_all(raw_text, "\r\n\r\n\r\n","")
      
      extra_text <- raw_text %>%
        str_replace_all(., "—", "\r\n\n") %>%
        str_replace_all(., "Pets:", "Pets:\n") %>%
        str_replace_all(., "Fees:", "Fees:\n") 
      
      cat(extra_text)
      
      
      #Upload Description Text
      ###################
      remDr$navigate(url_data)
      Sys.sleep(10)
      
      #view screenshot of browser window (automate by finding how to get view browser window as code executes)
      remDr$screenshot(display = TRUE, useViewer = TRUE, file = NULL)
      
      
      
      
      remDr$findElements("class", "read-more_button")[[1]]$clickElement()
      
      Sys.sleep(5) # give the page time to fully load
      html <- remDr$getPageSource()[[1]]
      
      # extract street number, name, city, state and zip fields
      street_num <- read_html(html) %>% # parse HTML
        html_nodes("h1") %>%# extract table nodes with class = "tbl_mapReception"
        html_text  %>%
        str_replace(., "LaSalle", "La Salle") %>%
        print()
      
      
      # extract # of bedrooms field
      
      bedrooms_num <- read_html(html) %>% # parse HTML
        html_nodes(".item:nth-child(1) .value") %>%# extract table nodes with class = "tbl_mapReception"
        html_text %>% # have rvest turn it into a dataframe
        as.numeric() %>%
        print()
      
      # extract # of bathrooms field
      
      bathrooms_num <- read_html(html) %>% # parse HTML
        html_nodes(".item:nth-child(2) .value") %>%# extract table nodes with class = "tbl_mapReception"
        html_text %>% # have rvest turn it into a dataframe
        as.numeric() %>%
        print()
      
      #change na to zero
      if(is.na(bedrooms_num)){
        bedrooms_num <- 0
      }
      
      
      laundry <- read_html(html) %>% # parse HTML
        html_nodes(".col-lg-8") %>%# extract table nodes with class = "tbl_mapReception"
        html_text %>% # have rvest turn it into a dataframe
        #  as.numeric() %>%
        print()
      #find match for LaundryIn Unit
      #Click LaundryIn Unit Button
      In_unit_laundry <- str_detect(laundry, "LaundryIn Unit") %>%
        print()
      
      Laundry_in_building <- str_detect(laundry, "Shared in Building") %>%
        print()
      
      Heating_type <- read_html(html) %>% # parse HTML
        html_nodes("#listingOverview .medium") %>% # extract table nodes 
        html_text %>% # have rvest turn it into a dataframe
        #  as.numeric() %>%
        print()
      
      Radiator_heating <- str_detect(Heating_type, "Radiator") %>%
        print()
      
      Gas_heating <- str_detect(Heating_type, "Gas") %>%
        print()
      
      
      
      
      
      # extract price field
      
      price <- read_html(html) %>% # parse HTML
        html_nodes(".s-listing_content-top-price") %>%# extract table nodes with class = "tbl_mapReception"
        html_text %>%
        str_remove(., "/mo")  %>%
        str_remove(., "\\$")  %>%
        print()
      
      
      # extract date available field
      
      date_avaiable <- read_html(html) %>% # parse HTML
        html_nodes("#s-listing-cart > div > section.s-listing_content > div > div > div.col-md-7.col-lg-8 > div > div.s-listing_content-top > div.s-listing_content-top-info > div.s-listing_content-top-details > div:nth-child(3) > p.value") %>%# extract table nodes with class = "tbl_mapReception")
        html_text  
      
      
      #change 'Now' to today's date 
      #Change date to specific date if actual date is returned (not "Now")
      if(date_avaiable == "Now"){
        ## locale-specific version of date()
        date_avaiable <- format(Sys.time(), "%m %d %Y") 
      } else {
        date_avaiable <- date_avaiable %>%
          paste("2023") %>% #paste in the year (update annually) %>%
          str_replace(., " ", "/") %>%
          mdy()  %>%
          print()
        date_avaiable <-  format(date_avaiable, "%b-%d-%Y")
        
      }
      
      
      #Add text to date string
      date_avaiable <-paste("\nDate Available", date_avaiable)
      
      
      
      
      #  
      
      
      
      
      
      
      # extract description field
      description <- read_html(html) %>% # parse HTML
        html_nodes('#read-more-listing > div > p') %>%# extract table nodes with class = "tbl_mapReception"
        html_text # have rvest turn it into a dataframe
      description_text <- description[[1]][1] %>%
        as.character() %>%
        #paste("\n") %>%
        print()
      
      description_text <- paste("\n", description_text, sep = )  
      #add space to beginning of string
      #Append date string to beginning of description string
      
      #description_text <-  paste(date_avaiable, description_text)
      
      
      
      
      description_text <- paste(date_avaiable,description_text,sep="\n", collapse=NULL)
      
      description_text <- paste(description_text, url_data, sep="\n")
      
      description_text <- paste(street_num, description_text, sep="\n")
      
      #description_text <- str_squish(description_text)
      
      description_text <- paste(description_text,extra_text) %>%
        str_replace_all(., "Pictures, layout, and finishes may differ or be of a similar unit available within the building.", "") 
      
      
      
      
      
      
      
      
      # extract rental detail header fields
      rental_details <- read_html(html) %>% # parse HTML
        html_nodes(".grid") %>%
        html_text %>%
        #str_squish() %>%
        #str_replace_all(.,",", "") %>% # remove commas in value 
        #strsplit(., split = " ") %>%
        print()
      #find match for Cats OK
      #Click Cat Friendly Button
      cats <- str_detect(rental_details, "Cats OK") %>%
        print()
      
      #find match for Cats OK
      #Click dog Friendly Button
      dogs <- str_detect(rental_details, "Dogs OK") %>%
        print()
      
      #find match for garage parking
      #Garage Parking default for FM
      Garage_parking <- str_detect(rental_details, "Garage") %>%
        print()
      
      #find match for Outdoor parking
      #Off-Steet Parking default for FM
      Off_street_parking <- str_detect(rental_details, "Assigned Outdoor Parking") %>%
        print()
      
      #find match for Indoor parking
      #Garage Parking default for FM
      Garage_parking_dup <- str_detect(rental_details, "Assigned Indoor Parking") %>%
        print()
      #find match for a/c
      
      cooling <- read_html(html) %>% # parse HTML
        html_nodes(".s-listing_content-overview-item:nth-child(6)") %>%
        html_text %>% # have rvest turn it into a dataframe
        #  as.numeric() %>%
        print()
      
      Central_AC <- str_detect(cooling, "Central A/C") %>%
        print()
      
      
      AC_available <- str_detect(cooling, "Window / Wall A/C") %>%
        print()
      
      #create tibble
      fulton_data <- data.frame(bedrooms_num, 
                                bathrooms_num,
                                price,
                                street_num,
                                description_text,
                                date_avaiable,
                                In_unit_laundry,
                                Laundry_in_building,
                                Garage_parking,
                                Garage_parking_dup,
                                Off_street_parking,
                                Central_AC,
                                AC_available,
                                Radiator_heating,
                                Gas_heating,
                                cats,
                                dogs)
      #export to csv
      write_csv(fulton_data , file = "C:/Users/Open/Documents/FultonGrace/FultonGrace/Phase1//fulton_data.csv")
      
      # extract images field
      img <- read_html(html) %>% # parse HTML
        html_nodes("img") %>%
        html_attr('data-src') %>%
        discard(., is.na) %>%
        print()
      
      # read images from url
      
      
      download.file(img, destfile = basename(img), mode = 'wb') %>% #When you download binary files, you have to specify the mode to be binary, e.g.
        print(.,)
      
      #close session
      remDr$close()
      
      # stop the selenium server
      rm(remDr)
      
      
      # Long Running Task
      Sys.sleep(1)
      
      # Update progress
      incProgress(1/N)
    }})

  

    
  
})

    
#############################################
    # Run after confirming that no more than 10 photos are in the IMG Folder
    ###########################################
  observeEvent(input$Phase_2, {  
    file_vector <- list.files(path = "C:/Users/Open/Documents/FultonGrace/FultonGrace/IMG")
    
    p <- paste0("C:\\\\Users\\\\Open\\\\Documents\\\\FultonGrace\\\\FultonGrace\\IMG\\\\", file_vector)
    
    #remove whitespace
    r <-  gsub(" ", "", p, fixed = TRUE)
    
    #convert to dataframe
    t <- as.data.frame(r)
    
    #export to csv
    write_csv(t , file = "C:/Users/Open/Documents/FultonGrace/FultonGrace/Phase1//fulton_statement_data.csv")
    
    
    #Run python script to post to FaceBook MarketPlace
    # RUN IF #IMG IS 10
    
    system(paste('C:/Users/Open/AppData/Local/Programs/Python/Python39/python.exe',
                 'C:/Users/Open/Documents/FultonGrace/FultonGrace/Phase2/fulton/Scripts/Facebook_Marketplace.py'))
    
    
    # run after posting to social media to clear folder for next batch
    # file_names <- sprintf("C:/Users/Open/Documents/FultonGrace/FultonGrace/IMG/%s",  file_vector)
    #  file.remove(file_names)   # Apply file.remove
    
    
    system("docker stop 8598164f201230fdb9abca60c40fab4a5e0a296fe6a8cddcbe2728502be5e92a")
    ################################################
    
})
}  

shinyApp(ui, server)
    








