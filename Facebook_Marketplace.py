
# Python program to demonstrate
# selenium




from selenium import webdriver
import pandas as pd
import pandas
import csv
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import os
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
import unittest
from selenium.webdriver.support.ui import Select


#import java.util.concurrent.TimeUnit
#import java
import pyautogui
from os import listdir
from os.path import isfile, join
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time

#import csv appartment data from Rscript

df = pd.read_csv('C:\\Users\\Open\\Documents\\FultonGrace\\FultonGrace\\Phase1\\fulton_data.csv')
#df_1 = pd.read_csv('C:\\Users\\Open\\Documents\\FultonGrace\\FultonGrace\\Phase1\\fulton_statement_data.csv')

#convert to character string so send_keys
df['bedrooms_num'] = df.bedrooms_num.astype(str)
df['bathrooms_num'] = df.bathrooms_num.astype(str)
df['price'] = df.price.astype(str)
df['street_num'] = df.street_num.astype(str)
df['description_text'] = df.description_text.astype(str)
df['date_avaiable'] = df.date_avaiable.astype(str)




#print column names

# Access a single value from the DataFrame
beds = df.at[0, 'bedrooms_num']
baths = df.at[0, 'bathrooms_num']
price = df.at[0, 'price']
address = df.at[0, 'street_num']
description = df.at[0, 'description_text']
date = df.at[0, 'date_avaiable']
in_unit = df.at[0, 'In_unit_laundry']
in_building = df.at[0, 'Laundry_in_building']
garage_p = df.at[0, 'Garage_parking']
Indoor_p = df.at[0, 'Garage_parking_dup']
off_p = df.at[0, 'Off_street_parking']
cen_AC = df.at[0, 'Central_AC']
avail_AC = df.at[0, 'AC_available']
rad = df.at[0, 'Radiator_heating']
gas = df.at[0, 'Gas_heating']
cat = df.at[0, 'cats']
dog = df.at[0, 'dogs']





print(beds)

#options = Options()
#options.add_argument("start-maximized")
#options.add_argument("--disable-infobars")
#options.add_argument("start-maximized")
#options.add_argument("--disable-extensions")
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 25)

#binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')

def main():
    driver.maximize_window()
    #driver.execute_script("document.body.style.zoom='10%'")


if __name__ == '__main__':
    main()


#driver.implicitly_wait(10)


#driver.maximize_window()

# set implicit wait time
#driver.implicitly_wait(10) # seconds
driver.get("https://www.facebook.com/login/device-based/regular/login/?login_attempt=1")

# find element for User ID box
user_ID_box = driver.find_element(By.XPATH, '//*[@id="email"]')

# send user name (email) to user_ID_box

# send username to the UserID box
user_ID_box.send_keys("7085069967")

# give page to load
#time.sleep(5)

# find element for password field
PasswordBox = driver.find_element(By.CSS_SELECTOR, '#pass')
# send password password field
PasswordBox.send_keys("198806!Sar!!!")

#find element for log-in button

log_in = driver.find_element(By.XPATH, '//*[@id="loginbutton"]')

#click the log -in button
log_in.click()

# give page time to fully load
time.sleep(35)


driver.get("https://www.facebook.com/marketplace/create/rental")





time.sleep(5)




#pyautogui.hotkey('ctrl', '-') #zooms out to 30%
#pyautogui.hotkey('ctrl', '-')
#pyautogui.hotkey('ctrl', '-')
#pyautogui.hotkey('ctrl', '-')
#pyautogui.hotkey('ctrl', '-')



#WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//input[@type='file']")))

#wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys("C:/Users/Open/Documents/FultonGrace/FultonGrace/IMG/1684527241-2023_3_27_3933_N_Janssen_Unit_2S_18.jpg")
#gather file names from IMG folder
path = "C:\\Users\\Open\\Documents\\FultonGrace\\FultonGrace\\IMG\\"
dir_list =  os.listdir(path)

#print(dir_list)

# slicing the list so 'geckdriver log' is not uploaded to images field in facebook marketplace
dir_list_sin_gecko= dir_list[:-1]

#print(dir_list_sin_gecko)


#paste file directory into each element of list with file names
result = [path + direction for direction in dir_list_sin_gecko]

    




#time.sleep(5)

#############################################################################################################################################################################################################
#upload photos
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys('C:\\Users\\Open\\Documents\\FultonGrace\\FultonGrace\IMG\\1693930094-1626186274-1626186209-1623776460-1623776421-1620917527-1615992738-1615992690-1615992647-1615992629-1613398778-85034_981618.jpg')
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys('C:\\Users\\Open\\Documents\\FultonGrace\\FultonGrace\IMG\\1693930094-1626186274-1626186209-1623776460-1623776421-1620917528-1615992738-1615992691-1615992647-1615992629-1613398779-85034_981619.jpg')
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys('C:\\Users\\Open\\Documents\\FultonGrace\\FultonGrace\IMG\\1693930094-1626186274-1626186210-1623776460-1623776421-1620917528-1615992738-1615992691-1615992647-1615992630-1613398779-85034_981620.jpg')
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys('C:\\Users\\Open\\Documents\\FultonGrace\\FultonGrace\IMG\\1693930095-1626186274-1626186210-1623776460-1623776421-1620917528-1615992738-1615992691-1615992647-1615992630-1613398780-85034_981621.jpg')
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys('C:\\Users\\Open\\Documents\\FultonGrace\\FultonGrace\IMG\\1693930095-1626186275-1626186210-1623776460-1623776421-1620917528-1615992739-1615992691-1615992648-1615992630-1613398780-85034_981622.jpg')
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys('C:\\Users\\Open\\Documents\\FultonGrace\\FultonGrace\IMG\\1693930095-1626186275-1626186210-1623776461-1623776422-1620917528-1615992739-1615992692-1615992648-1615992630-1613398780-85034_981623.jpg')
#############################################################################################################################################################################################################

#wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(file1)
#wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(file2)
#wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(file3)
#wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(file4)
#wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(file5)
#wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(file6)
#wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(file7)
#wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(file8)
#wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(file9)
#wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))).send_keys(file10)

#path to clear duplicates##########################################
dup1 = ".xsgj6o6:nth-child(1) .x1yrsyyn"

#get count of files in IMG folder
dir_path = r'C:\Users\Open\Documents\FultonGrace\FultonGrace\IMG'
count = 0
# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        count += 1
img_count = (count - 1) # '3' is assuming that geckdriver, R History and R data files are in IMG folder

#remove duplicate uploads

#upload 10 photos
if img_count == 10:
  x = list(range(44+1))  # if you want a real list

#upload 9 photos
if img_count == 9:
  x = list(range(35+1))  # if you want a real list

#upload 8 photos
if img_count == 8:
  x = list(range(27+1))  # if you want a real list

#upload 7 photos
if img_count == 7:
  x = list(range(20+1))  # if you want a real list
  
#upload 6 photos
if img_count == 6:
  x = list(range(14+1))  # if you want a real list
  
#upload 5 photos
if img_count == 5:
  x = list(range(9+1))  # if you want a real list
  
#upload 4 photos
if img_count == 4:
  x = list(range(5+1))  # if you want a real list
  
#upload 3 photos
if img_count == 3:
  x = list(range(2+1))  # if you want a real list
  
#upload 2 photos
if img_count == 2:
  x = list(range(1))  # if you want a real list
  
#upload 1 photos
if img_count == 1:
  x = list(range(44+1))  # if you want a real list
  
  
  


for i in x:
  wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, dup1))).click()
  time.sleep(0.25) #sleep for 250 milliseconds
  
#scroll element for 'Home for Sale or Rent' into viewport 

sale_rent = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[4]/div/div/label/div/div[1]/div/div'
sale_rent_scroll = driver.find_element(By.XPATH, sale_rent)

#inject javascript to scroll button into view of viewport before interacting 
driver.execute_script("arguments[0].scrollIntoView(true);", sale_rent_scroll)

sale_rent = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[4]/div/div/label/div/div[1]/div/div"
rent = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/div[1]'

#Click Home for Sale or Rent Button
wait.until(EC.presence_of_element_located((By.XPATH, sale_rent))).click()

#Click 'Rent" from drop down box
wait.until(EC.presence_of_element_located((By.XPATH, rent))).click()

rental_type = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[5]/div/div/div/label/div/div[1]/div/div"
apartment = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/div[1]/div/div/span"
#click Rental type Button
wait.until(EC.presence_of_element_located((By.XPATH, rental_type))).click()
wait.until(EC.presence_of_element_located((By.XPATH, apartment))).click()

#Fill in # of bedrooms
#bedrooms_num 
#bed_scroll = driver.find_element((By.XPATH, '//*[(@id = "\:r1a\:")]')


#driver.execute_script("arguments[0].scrollIntoView(true);", bed_scroll)

#wait.until(EC.element_to_be_clickable(((By.XPATH, '//*[(@id = "\:r1a\:")]'))).click()

#time.sleep(5) #sleep for 250 milliseconds



#scroll beds field into view
beds_scroll = driver.find_element(By.XPATH, "//input[@type='text']")









driver.execute_script("arguments[0].scrollIntoView(true);", beds_scroll)

wait.until(EC.presence_of_element_located((By.XPATH,"//input[@type='text']"))).send_keys(beds)

#scroll bath into view

baths_scroll = driver.find_element(By.XPATH,'//*[@class="x1i10hfl xggy1nq x1s07b3s x1kdt53j x1a2a7pz xjbqb8w x76ihet xwmqs3e x112ta8 xxxdfa6 x9f619 xzsf02u x1uxerd5 x1fcty0u x132q4wb x1a8lsjc x1pi30zi x1swvt13 x9desvi xh8yej3 x15h3p50 x10emqs4"]')

driver.execute_script("arguments[0].scrollIntoView(true);", baths_scroll)

#Fill in # of bathrooms
wait.until(EC.presence_of_element_located((By.XPATH,'(//*[@class="x1i10hfl xggy1nq x1s07b3s x1kdt53j x1a2a7pz xjbqb8w x76ihet xwmqs3e x112ta8 xxxdfa6 x9f619 xzsf02u x1uxerd5 x1fcty0u x132q4wb x1a8lsjc x1pi30zi x1swvt13 x9desvi xh8yej3 x15h3p50 x10emqs4"])[2]'))).send_keys(baths)



#scroll price field into view
price_scroll = driver.find_element(By.XPATH,'(//*[@class="x1i10hfl xggy1nq x1s07b3s x1kdt53j x1a2a7pz xjbqb8w x76ihet xwmqs3e x112ta8 xxxdfa6 x9f619 xzsf02u x1uxerd5 x1fcty0u x132q4wb x1a8lsjc x1pi30zi x1swvt13 x9desvi xh8yej3 x15h3p50 x10emqs4"])[3]')


driver.execute_script("arguments[0].scrollIntoView(true);", price_scroll)


#Fill in # of price

wait.until(EC.presence_of_element_located((By.XPATH,'(//*[@class="x1i10hfl xggy1nq x1s07b3s x1kdt53j x1a2a7pz xjbqb8w x76ihet xwmqs3e x112ta8 xxxdfa6 x9f619 xzsf02u x1uxerd5 x1fcty0u x132q4wb x1a8lsjc x1pi30zi x1swvt13 x9desvi xh8yej3 x15h3p50 x10emqs4"])[3]'))).send_keys(price)

#scroll address field into view
address_scroll = driver.find_element(By.XPATH,'(//*[@class="x1i10hfl xggy1nq x1s07b3s x1kdt53j x1a2a7pz xjbqb8w x76ihet xwmqs3e x112ta8 xxxdfa6 x9f619 xzsf02u x1uxerd5 x1fcty0u x132q4wb x1a8lsjc x1pi30zi x1swvt13 x9desvi xh8yej3 x15h3p50 x10emqs4"])[4]')


driver.execute_script("arguments[0].scrollIntoView(true);", address_scroll)

#property address field
wait.until(EC.presence_of_element_located((By.XPATH,'(//*[@class="x1i10hfl xggy1nq x1s07b3s x1kdt53j x1a2a7pz xjbqb8w x76ihet xwmqs3e x112ta8 xxxdfa6 x9f619 xzsf02u x1uxerd5 x1fcty0u x132q4wb x1a8lsjc x1pi30zi x1swvt13 x9desvi xh8yej3 x15h3p50 x10emqs4"])[4]'))).send_keys(address)


# find id of first option in address field
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/div/ul/li[1]'))).click()


#scroll description field into view
description_scroll = driver.find_element(By.XPATH,'//*[@class="x1i10hfl xggy1nq x1s07b3s xjbqb8w x76ihet xwmqs3e x112ta8 xxxdfa6 x9f619 xzsf02u x78zum5 x1jchvi3 x1fcty0u x132q4wb xyorhqc xaqh0s9 x1a2a7pz x6ikm8r x10wlt62 x1pi30zi x1swvt13 xtt52l0 xh8yej3"]')


driver.execute_script("arguments[0].scrollIntoView(true);", description_scroll)

#Fill in  description
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@class="x1i10hfl xggy1nq x1s07b3s xjbqb8w x76ihet xwmqs3e x112ta8 xxxdfa6 x9f619 xzsf02u x78zum5 x1jchvi3 x1fcty0u x132q4wb xyorhqc xaqh0s9 x1a2a7pz x6ikm8r x10wlt62 x1pi30zi x1swvt13 xtt52l0 xh8yej3"]'))).send_keys(description)


#scroll date field into view
date_scroll = driver.find_element(By.XPATH,'//*[@class="x1i10hfl xggy1nq x1s07b3s xjbqb8w x76ihet xwmqs3e x112ta8 xxxdfa6 x9f619 xzsf02u x78zum5 x1jchvi3 x1fcty0u x132q4wb xyorhqc xaqh0s9 x1a2a7pz x6ikm8r x10wlt62 x1pi30zi x1swvt13 xtt52l0 xh8yej3"]')


driver.execute_script("arguments[0].scrollIntoView(true);", date_scroll)

#Fill in  date
#wait.until(EC.presence_of_element_located((By.XPATH,'//*[@class="x1i10hfl xggy1nq x1s07b3s xjbqb8w x76ihet xwmqs3e x112ta8 xxxdfa6 x9f619 xzsf02u x78zum5 x1jchvi3 x1fcty0u x132q4wb xyorhqc xaqh0s9 x1a2a7pz x6ikm8r x10wlt62 x1pi30zi x1swvt13 xtt52l0 xh8yej3"]'))).send_keys(date)




############################################################################################
#scroll element for 'Home for Sale or Rent' into viewport 

laundry_type = '//*[@class="xjyslct xjbqb8w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xzsf02u x78zum5 x1jchvi3 x1fcty0u x132q4wb xdj266r x11i5rnm xat24cr x1mh8g0r x1a2a7pz x9desvi x1pi30zi x1a8lsjc x1swvt13 x1n2onr6 x16tdsg8 xh8yej3 x1ja2u2z"]'
laundry_type_scroll = driver.find_element(By.XPATH, laundry_type)

#inject javascript to scroll button into view of viewport before interacting 
driver.execute_script("arguments[0].scrollIntoView(true);", laundry_type_scroll)

laundry_type = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[15]/div/div/label/div/div[1]/div/div'
in_unit_type = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]'

#Click Home for Sale or in_unit_type Button
wait.until(EC.presence_of_element_located((By.XPATH, laundry_type))).click()

if in_unit:
#Click 'in_unit_type" from drop down box
#wait.until(EC.presence_of_element_located((By.XPATH, in_unit_type))).click()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, in_unit_type))).click()
  

in_building_type = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[2]'  
if in_building:
#Click 'in_unit_type" from drop down box
#wait.until(EC.presence_of_element_located((By.XPATH, in_unit_type))).click()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, in_building_type))).click()

############################################
parking_type = '(//*[@class="xjyslct xjbqb8w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xzsf02u x78zum5 x1jchvi3 x1fcty0u x132q4wb xdj266r x11i5rnm xat24cr x1mh8g0r x1a2a7pz x9desvi x1pi30zi x1a8lsjc x1swvt13 x1n2onr6 x16tdsg8 xh8yej3 x1ja2u2z"])[4]'
parking_available = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[4]'
#Click parking type Button
wait.until(EC.presence_of_element_located((By.XPATH, parking_type))).click()



if garage_p:
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, parking_available))).click()
  
if Indoor_p:
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, parking_available))).click()
  
if off_p:
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, parking_available))).click()
###################  
ac_type = '(//*[@class="xjyslct xjbqb8w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xzsf02u x78zum5 x1jchvi3 x1fcty0u x132q4wb xdj266r x11i5rnm xat24cr x1mh8g0r x1a2a7pz x9desvi x1pi30zi x1a8lsjc x1swvt13 x1n2onr6 x16tdsg8 xh8yej3 x1ja2u2z"])[5]'
ac_available = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[2]'
#Click ac type Button
wait.until(EC.presence_of_element_located((By.XPATH, ac_type))).click()

if avail_AC:
  wait.until(EC.presence_of_element_located((By.XPATH, ac_available))).click()
  
if cen_AC:
  wait.until(EC.presence_of_element_located((By.XPATH, ac_available))).click()

###################  
heat_type = '(//*[@class="xjyslct xjbqb8w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xzsf02u x78zum5 x1jchvi3 x1fcty0u x132q4wb xdj266r x11i5rnm xat24cr x1mh8g0r x1a2a7pz x9desvi x1pi30zi x1a8lsjc x1swvt13 x1n2onr6 x16tdsg8 xh8yej3 x1ja2u2z"])[6]'
heat_available = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[2]'
#Click heat type Button
wait.until(EC.presence_of_element_located((By.XPATH, heat_type))).click()

if gas:
  wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[3]/div[1]/div/div/span'))).click()
  
if rad:
  wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[4]/div[1]/div/div/span'))).click()

###################  

if cat:
  wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[19]/div/div/input'))).click()

dog_scroll = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[20]/div/div/input')


driver.execute_script("arguments[0].scrollIntoView(true);", dog_scroll)
  
  
if dog:
  wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div/div[20]/div/div/input'))).click()

  
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.x6s0dn4:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)'))).click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.x6s0dn4:nth-child(4) > div:nth-child(2) > div:nth-child(1)'))).click()
  





#driver.quit()  


  
  
