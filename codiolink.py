# make sure to have chrome web driver installed in the same folder for ease of access
import loginkeys
import pandas as pd
from selenium import webdriver
import numpy as py
from time import sleep 
from selenium.webdriver.common.keys import Keys
import csv
#stuff needed to make this work

file1 = open('codiolink.txt', 'a') 
videohandle = pd.read_csv(r'C:\Users\garam masala 3.0\Desktop\canvastoedx\video list.csv')
# fhand for video list, not needed in this instance
dataframe = pd.DataFrame(videohandle, columns=['Module: Segment', 'Working Title', 'Video File','Caption File','Codio Link' ])


driver_location = (r'C:\Users\garam masala 3.0\Desktop\canvastoedx\chromedriver.exe')
# location of the webdriver, make sure that the version your current chrome is the same version of the webdriver
driver = webdriver.Chrome(driver_location)

driver.get(loginkeys.canvasurl)
# course url

# LOGIN process begins
sleep(3)
driver.find_element_by_id('username').click()
driver.find_element_by_id('username').send_keys(loginkeys.calnetemail)
driver.find_element_by_id('password').click()
driver.find_element_by_id('password').send_keys(loginkeys.calnetpassword)
sleep(2)
driver.find_element_by_id('submit').click()

# please auth manually through duo mobile
print("Please log in through Duo Mobile manually.")
print("Please log in through Duo Mobile manually.")
print("Please log in through Duo Mobile manually.")
print("Please log in through Duo Mobile manually.")
print("Please log in through Duo Mobile manually.")
print("You have 20 seconds to authenticate.")

# navigate to modules, use if statement in real thing
#USE XPATH FINDER EXTENSION
sleep(20)
driver.find_element_by_xpath('//*[@title="Modules"]').click()
sleep(5)

modulelink = driver.find_elements_by_class_name("for-nvda")
for link in modulelink:
    driver.switch_to.window(driver.window_handles[0])
    # print(link.get_attribute("href"))
    main_window = driver.current_window_handle
    templink = link.get_attribute("href")
    title = link.get_attribute("aria-label")
    driver.execute_script("window.open('','_blank');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(templink)
    # open and close each module link/listref in new tab to scrape
    try:
        # codio link try
        codiolink = driver.find_element_by_xpath('.//*[@class="hide"]//button').click()
        driver.switch_to.window(driver.window_handles[2])
        tile = title[:4].rstrip()
        codiourl = str(driver.current_url)
        print(tile)
        print(codiourl)
        # file1.write(tile + codiourl)
        driver.switch_to.window(driver.window_handles[2])
        driver.close()
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
    except:
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        
# need to save dataframe as csv
# videohandle.to_csv('video list.csv', index=False)