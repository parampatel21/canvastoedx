# make sure to have chrome web driver installed in the same folder for ease of access
import loginkeys
import pandas as pd
from selenium import webdriver
import numpy as py
from time import sleep 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#stuff needed to make this work

videohandle = pd.read_csv(r'C:\Users\usernamehere\\video list.csv')
# READS CSV, MAKE SURE YOUR CSV IS SET TO THE RIGHT DIRECTORY

driver_location = (r'C:\Users\usernamehere\chromedriver.exe')
# location of the webdriver, make sure that the version your current chrome is the same version of the webdriver

driver = webdriver.Chrome(driver_location)
url = loginkeys.edxurl
driver.get(url)
sleep(2)
# URL GETTER


# LOGIN SEQUENCE
driver.find_element_by_id('login-email').click()
driver.find_element_by_id('login-email').send_keys(loginkeys.edxemail)
driver.find_element_by_id('login-password').click()
driver.find_element_by_id('login-password').send_keys(loginkeys.edxpassword)
driver.find_element_by_xpath(".//*[@type='submit']").click()
sleep(8)
# END LOGIN SEQUENCE


# FUNCTIONS
def deletesections():
    print("Deleting all modules for a clean 'canvas'.")
    for i in range(0 ,len(videohandle)):
        try:
            driver.find_element_by_xpath("(.//*[@class='icon fa fa-trash-o'])").click()
            sleep(0.25)
            driver.find_element_by_xpath("//button[contains(text(),'Yes, delete this section')]").click()
            sleep(0.25)
        except:
            pass
# END FUNCTIONS


# INPUT SEQUENCE
deletesections()
moduleno = 0
subsection = 0
unitno = 1
unitno2 = -1
x = 1
y = 1
z = 1
for i in range(0, len(videohandle)):
    modulename = str(videohandle[loginkeys.column1][i])
    # CREATES MODULE ENTRY
    if (modulename.startswith("Module")):
        sleep(4)
        moduleno = moduleno + 1
        driver.find_element_by_xpath(".//*[@title='Click to add a new Section']").click()
        sleep(4)
        driver.find_element_by_xpath("(.//*[@class='section-header']//input)" + str([moduleno])).send_keys(videohandle[loginkeys.column1][i])
        sleep(2)
        try:
            driver.find_element_by_xpath(".//*[@class='footer-content-primary']").click()
        except:
            continue
        #TODO FIX THIS PUBLISH ERROR
        sleep(2)

    # IF MODULE 1
    if (modulename.startswith("1")):
        sleep(4)
        try: 
        # [1] here
            sleep(2)
            driver.find_element_by_xpath("(.//*[@title='Click to add a new Subsection'])[1]").click()
            sleep(2)
            driver.find_element_by_xpath("(.//*[@class='icon fa fa-pencil'])" + str([i + 1])).click()
            sleep(1)
            actions = ActionChains(driver)
            actions.send_keys(str(videohandle[loginkeys.column1][i] + " - " + videohandle[loginkeys.column2][i]))
            actions.perform()
            sleep(7)
            driver.find_element_by_xpath(".//*[@class='footer-content-primary']").click()
            sleep(3)
            
        except:
            sleep(0.5)
            print("exception occurred")
            bactions = ActionChains(driver)
            bactions.send_keys(str(videohandle[loginkeys.column1][i] + " - " + videohandle[loginkeys.column2][i]))
            bactions.perform()
            sleep(7)
            driver.find_element_by_xpath(".//*[@class='footer-content-primary']").click()

        # INPUTTING UNIT INFO
        # VIDEO INPUT ENTRY
        videostring = str(videohandle[loginkeys.column3][i])
        srtstring = str(videohandle[loginkeys.column4][i])
        if (len(videostring) > 3):
            # [1] here
            try:
                unitno = unitno + 1
                driver.find_element_by_xpath("(.//*[@class='button button-new'])" + str([unitno])).click()
                sleep(3)
                unitname = driver.find_element_by_xpath(".//*[@type='text']")
            except:
                driver.execute_script("window.history.go(-1)")
                sleep(5)
                driver.find_element_by_xpath("(.//*[@class='icon fa fa-caret-down'])" + str([unitno])).click()
                sleep(2)
                driver.find_element_by_xpath("(.//*[@class='button button-new'])" + str([unitno])).click()
                print("backup sequence init")
                sleep(3)
                unitname = driver.find_element_by_xpath(".//*[@type='text']")
            unitname.send_keys(Keys.CONTROL, 'a')
            unitname.send_keys(Keys.BACKSPACE)
            sleep(1)
            unitname.send_keys("Video: " + str(videohandle[loginkeys.column2][i]))
            sleep(4)
            try:
                driver.find_element_by_xpath("(.//*[@type='button'])[5]").click()
                sleep(2)
                driver.find_element_by_xpath("(.//*[@class='header-actions']//span)[2]").click()
            except:
                driver.find_element_by_xpath("(.//*[@class='xblock-render']//span)[10]").click()
                sleep(2)
                try:
                    driver.find_element_by_xpath("(.//*[@class='header-actions']//span)[2]").click()
                except:
                    continue
            sleep(6)
            videofield = driver.find_element_by_xpath("(.//*[@class='wrapper-videolist-settings']//input)[1]")
            videofield.send_keys(Keys.CONTROL, 'a')
            videofield.send_keys(Keys.BACKSPACE)
            sleep(2)
            videofield.send_keys(videostring)
            sleep(4)
            try:
                driver.find_element_by_xpath("(//a[contains(text(),'Advanced')])[3]").click()
            except:
                driver.find_element_by_xpath("(//a[contains(text(),'Advanced')])[4]").click()
            sleep(4)
            displayname = driver.find_element_by_xpath("(.//*[@type='text'])[7]")
            displayname.send_keys(Keys.CONTROL, 'a')
            displayname.send_keys(Keys.BACKSPACE)
            sleep(2)
            displayname.send_keys("Video")
            sleep(2)
            driver.find_element_by_xpath("(.//*[@type='text'])[8]").send_keys(str(videohandle[loginkeys.column4][i]))
            sleep(4)
            driver.find_element_by_xpath("//a[contains(text(),'Save')]").click()
            sleep(4)
            driver.execute_script("window.history.go(-1)")
            sleep(25)

        # CODIO LINK ENTRY
        codiostring = str(videohandle[loginkeys.column5][i])
        if (len(codiostring) > 4):
            if (type(videohandle[loginkeys.column3][i]) is float):
                unitno = unitno + 1
                placeholder = "CHIPS - " + videohandle[loginkeys.column1][i]
            else:
                placeholder = "Reading: Section " + videohandle[loginkeys.column1][i]
            try:
                driver.find_element_by_xpath("(.//*[@class='icon fa fa-caret-down'])" + str([i + 1])).click()
                sleep(2)
                driver.find_element_by_xpath("(.//*[@class='button button-new'])" + str([unitno])).click()
                sleep(3)
            except:
                driver.find_element_by_xpath("(.//*[@class='icon fa fa-caret-down'])" + str([i + 1])).click()
                sleep(1)
                driver.find_element_by_xpath("(.//*[@class='button button-new'])" + str([unitno])).click()
                sleep(2)
            sleep(4)
            unitname = driver.find_element_by_xpath(".//*[@type='text']")
            unitname.send_keys(Keys.CONTROL, 'a')
            unitname.send_keys(Keys.BACKSPACE)
            sleep(1)
            unitname.send_keys(str(placeholder))
            sleep(4)
            try:
                driver.find_element_by_xpath("(.//*[@type='button']//span)[4]").click()
            except:
                driver.find_element_by_xpath("(.//*[@class='new-component']//span)[4]").click()
            sleep(5)
            try:
                driver.find_element_by_xpath("//span[contains(text(),'IFrame Tool')]").click()
            except:
                driver.find_element_by_xpath("(.//*[@class='name'])[7]").click()
            sleep(5)    
            driver.find_element_by_xpath("(//span[contains(text(),'Edit')])[3]").click()
            sleep(2)
            # delete sequeence HERERERERER
            sleep(4)
            driver.find_element_by_xpath("//button[contains(text(),'HTML')]").click()
            sleep(4)
            for i in range (0, 2392):
                try:
                    ActionChains(driver).send_keys(Keys.DELETE).perform()
                    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
                except:
                    print("deleting finished")
                        
            sleep(4)
            driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()
            sleep(4)
            driver.find_element_by_xpath("//button[contains(text(),'HTML')]").click()
            sleep(3)
            for i in range (0, 5):
                try:
                    ActionChains(driver).send_keys(Keys.DELETE).perform()
                    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
                except:
                    print("deleting finished")
            dactions = ActionChains(driver)
            sendkeys1 = str(videohandle[loginkeys.column2][unitno - 1])
            sendkeys2 = str(videohandle[loginkeys.column5][unitno - 1])
            dactions.send_keys('<h3 class="hd hd-2" style="text-align: center;">'+ sendkeys1 + '</h3>', Keys.ENTER)
            dactions.send_keys('<p style="text-align: center;"><iframe title="Codio Textbook" src="'+ sendkeys2 + '" width="100%" height="800" marginwidth="0" marginheight="0" frameborder="0" scrolling="no">', Keys.ENTER)
            dactions.send_keys('Your browser does not support IFrames.', Keys.ENTER)
            dactions.send_keys('</iframe></p>', Keys.ENTER)
            dactions.perform()
            sleep(4)
            driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()
            sleep(3)
            driver.find_element_by_xpath("//a[contains(text(),'Save')]").click()
            sleep(7)
            driver.get(loginkeys.edxurl)
            print("unitno - " + str(unitno))
            print("i - " + str(i))
            sleep(20)
    
        # IF MODULE 2
    if (modulename.startswith("2")):
        if x == 1:
            unitno = unitno + 1
            x = 0
        #change here
        sleep(4)
        try:
            sleep(2)
            driver.find_element_by_xpath("(.//*[@title='Click to add a new Subsection'])[2]").click()
            # change here
            sleep(2)
            driver.find_element_by_xpath("(.//*[@class='icon fa fa-pencil'])" + str([i + 1])).click()
            sleep(1)
            actions = ActionChains(driver)
            actions.send_keys(str(videohandle[loginkeys.column1][i] + " - " + videohandle[loginkeys.column2][i]))
            actions.perform()
            sleep(7)
            driver.find_element_by_xpath(".//*[@class='footer-content-primary']").click()
            sleep(3)
            
        except:
            sleep(0.5)
            print("exception occurred")
            bactions = ActionChains(driver)
            bactions.send_keys(str(videohandle[loginkeys.column1][i] + " - " + videohandle[loginkeys.column2][i]))
            bactions.perform()
            sleep(7)

        # INPUTTING UNIT INFO
        # VIDEO INPUT ENTRY
        videostring = str(videohandle[loginkeys.column3][unitno])
        srtstring = str(videohandle[loginkeys.column4][unitno])
        if (len(videostring) > 3):
            try:
                unitno = unitno + 1
                driver.find_element_by_xpath("(.//*[@class='button button-new'])" + str([unitno])).click()
                sleep(3)
                unitname = driver.find_element_by_xpath(".//*[@type='text']")
            except:
                driver.execute_script("window.history.go(-1)")
                sleep(5)
                driver.find_element_by_xpath("(.//*[@class='icon fa fa-caret-down'])" + str([unitno])).click()
                sleep(2)
                driver.find_element_by_xpath("(.//*[@class='button button-new'])" + str([unitno])).click()
                print("backup sequence init")
                sleep(4)
                unitname = driver.find_element_by_xpath(".//*[@type='text']")
            try:
                unitname.send_keys(Keys.CONTROL, 'a')
                unitname.send_keys(Keys.BACKSPACE)
                sleep(3)
                unitname.send_keys("Video: " + str(videohandle[loginkeys.column2][i]))
                sleep(4)
            except:
                sleep(2)
            try:
                driver.find_element_by_xpath("(.//*[@type='button'])[5]").click()
                sleep(2)
                driver.find_element_by_xpath("(.//*[@class='header-actions']//span)[2]").click()
            except:
                driver.find_element_by_xpath("(.//*[@class='xblock-render']//span)[10]").click()
                sleep(2)
                try:
                    driver.find_element_by_xpath("(.//*[@class='header-actions']//span)[2]").click()
                except:
                    continue
            sleep(6)
            videofield = driver.find_element_by_xpath("(.//*[@class='wrapper-videolist-settings']//input)[1]")
            videofield.send_keys(Keys.CONTROL, 'a')
            videofield.send_keys(Keys.BACKSPACE)
            sleep(2)
            videofield.send_keys(videostring)
            sleep(4)
            try:
                driver.find_element_by_xpath("(//a[contains(text(),'Advanced')])[3]").click()
            except:
                driver.find_element_by_xpath("(//a[contains(text(),'Advanced')])[4]").click()
            sleep(4)
            displayname = driver.find_element_by_xpath("(.//*[@type='text'])[7]")
            displayname.send_keys(Keys.CONTROL, 'a')
            displayname.send_keys(Keys.BACKSPACE)
            sleep(2)
            displayname.send_keys("Video")
            sleep(2)
            driver.find_element_by_xpath("(.//*[@type='text'])[8]").send_keys(str(videohandle[loginkeys.column4][i]))
            sleep(4)
            driver.find_element_by_xpath("//a[contains(text(),'Save')]").click()
            sleep(4)
            driver.execute_script("window.history.go(-1)")
            sleep(25)

        # CODIO LINK ENTRY
        codiostring = str(videohandle[loginkeys.column5][i])
        if (len(codiostring) > 4):
            if (type(videohandle[loginkeys.column3][i]) is float):
                unitno = unitno + 1
                placeholder = "CHIPS - " + videohandle[loginkeys.column1][i]
            else:
                placeholder = "Reading: Section " + videohandle[loginkeys.column1][i]
            try:
                driver.find_element_by_xpath("(.//*[@class='icon fa fa-caret-down'])" + str([i + 1])).click()
                sleep(2)
                driver.find_element_by_xpath("(.//*[@class='button button-new'])" + str([unitno])).click()
                sleep(3)
            except:
                driver.find_element_by_xpath("(.//*[@class='icon fa fa-caret-down'])" + str([i + 1])).click()
                sleep(1)
                driver.find_element_by_xpath("(.//*[@class='button button-new'])" + str([unitno])).click()
                sleep(2)
            sleep(4)
            unitname = driver.find_element_by_xpath(".//*[@type='text']")
            unitname.send_keys(Keys.CONTROL, 'a')
            unitname.send_keys(Keys.BACKSPACE)
            sleep(1)
            unitname.send_keys(str(placeholder))
            sleep(4)
            try:
                driver.find_element_by_xpath("(.//*[@type='button']//span)[4]").click()
            except:
                driver.find_element_by_xpath("(.//*[@class='new-component']//span)[4]").click()
            sleep(5)
            try:
                driver.find_element_by_xpath("//span[contains(text(),'IFrame Tool')]").click()
            except:
                driver.find_element_by_xpath("(.//*[@class='name'])[7]").click()
            sleep(5)    
            driver.find_element_by_xpath("(//span[contains(text(),'Edit')])[3]").click()
            sleep(2)
            # delete sequeence HERERERERER
            sleep(4)
            driver.find_element_by_xpath("//button[contains(text(),'HTML')]").click()
            sleep(4)
            for i in range (0, 2392):
                try:
                    ActionChains(driver).send_keys(Keys.DELETE).perform()
                    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
                except:
                    print("deleting finished")
                        
            sleep(4)
            driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()
            sleep(4)
            driver.find_element_by_xpath("//button[contains(text(),'HTML')]").click()
            sleep(3)
            for i in range (0, 5):
                try:
                    ActionChains(driver).send_keys(Keys.DELETE).perform()
                    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
                except:
                    print("deleting finished")
            dactions = ActionChains(driver)
            sendkeys1 = str(videohandle[loginkeys.column2][unitno - 1])
            sendkeys2 = str(videohandle[loginkeys.column5][unitno - 1])
            dactions.send_keys('<h3 class="hd hd-2" style="text-align: center;">'+ sendkeys1 + '</h3>', Keys.ENTER)
            dactions.send_keys('<p style="text-align: center;"><iframe title="Codio Textbook" src="'+ sendkeys2 + '" width="100%" height="800" marginwidth="0" marginheight="0" frameborder="0" scrolling="no">', Keys.ENTER)
            dactions.send_keys('Your browser does not support IFrames.', Keys.ENTER)
            dactions.send_keys('</iframe></p>', Keys.ENTER)
            dactions.perform()
            sleep(4)
            driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()
            sleep(3)
            driver.find_element_by_xpath("//a[contains(text(),'Save')]").click()
            sleep(7)
            driver.get(loginkeys.edxurl)
            print("unitno - " + str(unitno))
            print("i - " + str(i))
            sleep(20)
    if (modulename.startswith("3")):
        if y == 1:
            unitno = unitno + 1
            y = 0
        #change here
        sleep(4)
        try:
            sleep(2)
            driver.find_element_by_xpath("(.//*[@title='Click to add a new Subsection'])[3]").click()
            # change here
            sleep(2)
            driver.find_element_by_xpath("(.//*[@class='icon fa fa-pencil'])" + str([i + 1])).click()
            sleep(1)
            actions = ActionChains(driver)
            actions.send_keys(str(videohandle[loginkeys.column1][i] + " - " + videohandle[loginkeys.column2][i]))
            actions.perform()
            sleep(7)
            driver.find_element_by_xpath(".//*[@class='footer-content-primary']").click()
            sleep(3)
            
        except:
            sleep(0.5)
            print("exception occurred")
            bactions = ActionChains(driver)
            bactions.send_keys(str(videohandle[loginkeys.column1][i] + " - " + videohandle[loginkeys.column2][i]))
            bactions.perform()
            sleep(7)
            try:
                driver.find_element_by_xpath(".//*[@class='footer-content-primary']").click()
            except:
                continue
        # INPUTTING UNIT INFO
        # VIDEO INPUT ENTRY
        videostring = str(videohandle[loginkeys.column3][unitno])
        srtstring = str(videohandle[loginkeys.column4][unitno])
        if (len(videostring) > 3):
            try:
                unitno = unitno + 1
                driver.find_element_by_xpath("(.//*[@class='button button-new'])" + str([unitno])).click()
                sleep(3)
                unitname = driver.find_element_by_xpath(".//*[@type='text']")
            except:
                driver.execute_script("window.history.go(-1)")
                sleep(5)
                driver.find_element_by_xpath("(.//*[@class='icon fa fa-caret-down'])" + str([unitno])).click()
                sleep(2)
                driver.find_element_by_xpath("(.//*[@class='button button-new'])" + str([unitno])).click()
                print("backup sequence init")
                sleep(4)
                unitname = driver.find_element_by_xpath(".//*[@type='text']")
            try:
                unitname.send_keys(Keys.CONTROL, 'a')
                unitname.send_keys(Keys.BACKSPACE)
                sleep(3)
                unitname.send_keys("Video: " + str(videohandle[loginkeys.column2][i]))
                sleep(4)
            except:
                sleep(2)
            sleep(3)
            sleep(4)
            try:
                driver.find_element_by_xpath("(.//*[@type='button'])[5]").click()
                sleep(2)
                driver.find_element_by_xpath("(.//*[@class='header-actions']//span)[2]").click()
            except:
                driver.find_element_by_xpath("(.//*[@class='xblock-render']//span)[10]").click()
                sleep(2)
                try:
                    driver.find_element_by_xpath("(.//*[@class='header-actions']//span)[2]").click()
                except:
                    continue
            sleep(6)
            videofield = driver.find_element_by_xpath("(.//*[@class='wrapper-videolist-settings']//input)[1]")
            videofield.send_keys(Keys.CONTROL, 'a')
            videofield.send_keys(Keys.BACKSPACE)
            sleep(2)
            videofield.send_keys(videostring)
            sleep(4)
            try:
                driver.find_element_by_xpath("(//a[contains(text(),'Advanced')])[3]").click()
            except:
                driver.find_element_by_xpath("(//a[contains(text(),'Advanced')])[4]").click()
            sleep(4)
            displayname = driver.find_element_by_xpath("(.//*[@type='text'])[7]")
            displayname.send_keys(Keys.CONTROL, 'a')
            displayname.send_keys(Keys.BACKSPACE)
            sleep(2)
            displayname.send_keys("Video")
            sleep(2)
            driver.find_element_by_xpath("(.//*[@type='text'])[8]").send_keys(str(videohandle[loginkeys.column4][i]))
            sleep(4)
            driver.find_element_by_xpath("//a[contains(text(),'Save')]").click()
            sleep(4)
            driver.execute_script("window.history.go(-1)")
            sleep(25)

        # CODIO LINK ENTRY
        codiostring = str(videohandle[loginkeys.column5][i])
        if (len(codiostring) > 4):
            if (type(videohandle[loginkeys.column3][i]) is float):
                unitno = unitno + 1
                placeholder = "CHIPS - " + videohandle[loginkeys.column1][i]
            else:
                placeholder = "Reading: Section " + videohandle[loginkeys.column1][i]
            try:
                print(i)
                driver.find_element_by_xpath("(.//*[@class='icon fa fa-caret-down'])" + str([i + 1])).click()
                sleep(2)
                driver.find_element_by_xpath("(.//*[@class='button button-new'])" + str([unitno])).click()
                sleep(3)
            except:
                driver.find_element_by_xpath("(.//*[@class='icon fa fa-caret-down'])" + str([i + 1])).click()
                sleep(1)
                driver.find_element_by_xpath("(.//*[@class='button button-new'])" + str([unitno])).click()
                sleep(2)
            sleep(4)
            unitname = driver.find_element_by_xpath(".//*[@type='text']")
            unitname.send_keys(Keys.CONTROL, 'a')
            unitname.send_keys(Keys.BACKSPACE)
            sleep(1)
            unitname.send_keys(str(placeholder))
            sleep(4)
            try:
                driver.find_element_by_xpath("(.//*[@type='button']//span)[4]").click()
            except:
                driver.find_element_by_xpath("(.//*[@class='new-component']//span)[4]").click()
            sleep(5)
            try:
                driver.find_element_by_xpath("//span[contains(text(),'IFrame Tool')]").click()
            except:
                driver.find_element_by_xpath("(.//*[@class='name'])[7]").click()
            sleep(5)    
            driver.find_element_by_xpath("(//span[contains(text(),'Edit')])[3]").click()
            sleep(2)
            # delete sequeence HERERERERER
            sleep(4)
            driver.find_element_by_xpath("//button[contains(text(),'HTML')]").click()
            sleep(4)
            for i in range (0, 2392):
                try:
                    ActionChains(driver).send_keys(Keys.DELETE).perform()
                    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
                except:
                    print("deleting finished")
                        
            sleep(4)
            driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()
            sleep(4)
            driver.find_element_by_xpath("//button[contains(text(),'HTML')]").click()
            sleep(3)
            for i in range (0, 5):
                try:
                    ActionChains(driver).send_keys(Keys.DELETE).perform()
                    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
                except:
                    print("deleting finished")
            dactions = ActionChains(driver)
            sendkeys1 = str(videohandle[loginkeys.column2][unitno - 1])
            sendkeys2 = str(videohandle[loginkeys.column5][unitno - 1])
            dactions.send_keys('<h3 class="hd hd-2" style="text-align: center;">'+ sendkeys1 + '</h3>', Keys.ENTER)
            dactions.send_keys('<p style="text-align: center;"><iframe title="Codio Textbook" src="'+ sendkeys2 + '" width="100%" height="800" marginwidth="0" marginheight="0" frameborder="0" scrolling="no">', Keys.ENTER)
            dactions.send_keys('Your browser does not support IFrames.', Keys.ENTER)
            dactions.send_keys('</iframe></p>', Keys.ENTER)
            dactions.perform()
            sleep(4)
            driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()
            sleep(3)
            driver.find_element_by_xpath("//a[contains(text(),'Save')]").click()
            sleep(7)
            driver.get(loginkeys.edxurl)
            print("unitno - " + str(unitno))
            print("i - " + str(i))
            sleep(20)
    if (modulename.startswith("4")):
        if z == 1:
            unitno = unitno + 1
            z = 0
        #change here
        sleep(4)
        try:
            sleep(2)
            driver.find_element_by_xpath("(.//*[@title='Click to add a new Subsection'])[4]").click()
            # change here
            sleep(2)
            driver.find_element_by_xpath("(.//*[@class='icon fa fa-pencil'])" + str([i + 1])).click()
            sleep(1)
            actions = ActionChains(driver)
            actions.send_keys(str(videohandle[loginkeys.column1][i] + " - " + videohandle[loginkeys.column2][i]))
            actions.perform()
            sleep(7)
            driver.find_element_by_xpath(".//*[@class='footer-content-primary']").click()
            sleep(3)
            
        except:
            sleep(0.5)
            print("exception occurred")
            bactions = ActionChains(driver)
            bactions.send_keys(str(videohandle[loginkeys.column1][i] + " - " + videohandle[loginkeys.column2][i]))
            bactions.perform()
            sleep(7)
            driver.find_element_by_xpath(".//*[@class='footer-content-primary']").click()

        # INPUTTING UNIT INFO
        # VIDEO INPUT ENTRY
        videostring = str(videohandle[loginkeys.column3][unitno])
        srtstring = str(videohandle[loginkeys.column4][unitno])
        if (len(videostring) > 3):
            try:
                unitno = unitno + 1
                driver.find_element_by_xpath("(.//*[@class='button button-new'])" + str([unitno])).click()
                sleep(3)
                unitname = driver.find_element_by_xpath(".//*[@type='text']")
            except:
                driver.execute_script("window.history.go(-1)")
                sleep(5)
                driver.find_element_by_xpath("(.//*[@class='icon fa fa-caret-down'])" + str([unitno])).click()
                sleep(2)
                driver.find_element_by_xpath("(.//*[@class='button button-new'])" + str([unitno])).click()
                print("backup sequence init")
                sleep(4)
                unitname = driver.find_element_by_xpath(".//*[@type='text']")
            try:
                unitname.send_keys(Keys.CONTROL, 'a')
                unitname.send_keys(Keys.BACKSPACE)
                sleep(3)
                unitname.send_keys("Video: " + str(videohandle[loginkeys.column2][i]))
                sleep(4)
            except:
                sleep(2)
            sleep(7)
            try:
                driver.find_element_by_xpath("(.//*[@type='button'])[5]").click()
                sleep(2)
                driver.find_element_by_xpath("(.//*[@class='header-actions']//span)[2]").click()
            except:
                driver.find_element_by_xpath("(.//*[@class='xblock-render']//span)[10]").click()
                sleep(2)
                try:
                    driver.find_element_by_xpath("(.//*[@class='header-actions']//span)[2]").click()
                except:
                    continue
            sleep(6)
            videofield = driver.find_element_by_xpath("(.//*[@class='wrapper-videolist-settings']//input)[1]")
            videofield.send_keys(Keys.CONTROL, 'a')
            videofield.send_keys(Keys.BACKSPACE)
            sleep(2)
            videofield.send_keys(videostring)
            sleep(4)
            try:
                driver.find_element_by_xpath("(//a[contains(text(),'Advanced')])[3]").click()
            except:
                driver.find_element_by_xpath("(//a[contains(text(),'Advanced')])[4]").click()
            sleep(4)
            displayname = driver.find_element_by_xpath("(.//*[@type='text'])[7]")
            displayname.send_keys(Keys.CONTROL, 'a')
            displayname.send_keys(Keys.BACKSPACE)
            sleep(2)
            displayname.send_keys("Video")
            sleep(2)
            driver.find_element_by_xpath("(.//*[@type='text'])[8]").send_keys(str(videohandle[loginkeys.column4][i]))
            sleep(4)
            driver.find_element_by_xpath("//a[contains(text(),'Save')]").click()
            sleep(4)
            driver.execute_script("window.history.go(-1)")
            sleep(25)

        # CODIO LINK ENTRY
        codiostring = str(videohandle[loginkeys.column5][i])
        if (len(codiostring) > 4):
            if (type(videohandle[loginkeys.column3][i]) is float):
                unitno = unitno + 1
                placeholder = "CHIPS - " + videohandle[loginkeys.column1][i]
            else:
                placeholder = "Reading: Section " + videohandle[loginkeys.column1][i]
            try:
                driver.find_element_by_xpath("(.//*[@class='icon fa fa-caret-down'])" + str([i + 1])).click()
                sleep(2)
                driver.find_element_by_xpath("(.//*[@class='button button-new'])" + str([unitno])).click()
                sleep(3)
            except:
                driver.find_element_by_xpath("(.//*[@class='icon fa fa-caret-down'])" + str([i + 1])).click()
                sleep(1)
                driver.find_element_by_xpath("(.//*[@class='button button-new'])" + str([unitno])).click()
                sleep(2)
            sleep(4)
            unitname = driver.find_element_by_xpath(".//*[@type='text']")
            unitname.send_keys(Keys.CONTROL, 'a')
            unitname.send_keys(Keys.BACKSPACE)
            sleep(1)
            unitname.send_keys(str(placeholder))
            sleep(4)
            try:
                driver.find_element_by_xpath("(.//*[@type='button']//span)[4]").click()
            except:
                driver.find_element_by_xpath("(.//*[@class='new-component']//span)[4]").click()
            sleep(5)
            try:
                driver.find_element_by_xpath("//span[contains(text(),'IFrame Tool')]").click()
            except:
                driver.find_element_by_xpath("(.//*[@class='name'])[7]").click()
            sleep(5)    
            driver.find_element_by_xpath("(//span[contains(text(),'Edit')])[3]").click()
            sleep(2)
            # delete sequeence HERERERERER
            sleep(4)
            driver.find_element_by_xpath("//button[contains(text(),'HTML')]").click()
            sleep(4)
            for i in range (0, 2392):
                try:
                    ActionChains(driver).send_keys(Keys.DELETE).perform()
                    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
                except:
                    print("deleting finished")
                        
            sleep(4)
            driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()
            sleep(4)
            driver.find_element_by_xpath("//button[contains(text(),'HTML')]").click()
            sleep(3)
            for i in range (0, 5):
                try:
                    ActionChains(driver).send_keys(Keys.DELETE).perform()
                    ActionChains(driver).send_keys(Keys.BACKSPACE).perform()
                except:
                    print("deleting finished")
            dactions = ActionChains(driver)
            sendkeys1 = str(videohandle[loginkeys.column2][unitno - 1])
            sendkeys2 = str(videohandle[loginkeys.column5][unitno - 1])
            dactions.send_keys('<h3 class="hd hd-2" style="text-align: center;">'+ sendkeys1 + '</h3>', Keys.ENTER)
            dactions.send_keys('<p style="text-align: center;"><iframe title="Codio Textbook" src="'+ sendkeys2 + '" width="100%" height="800" marginwidth="0" marginheight="0" frameborder="0" scrolling="no">', Keys.ENTER)
            dactions.send_keys('Your browser does not support IFrames.', Keys.ENTER)
            dactions.send_keys('</iframe></p>', Keys.ENTER)
            dactions.perform()
            sleep(4)
            driver.find_element_by_xpath("//button[contains(text(),'OK')]").click()
            sleep(3)
            driver.find_element_by_xpath("//a[contains(text(),'Save')]").click()
            sleep(7)
            driver.get(loginkeys.edxurl)
            print("unitno - " + str(unitno))
            print("i - " + str(i))
            sleep(20)

# UPLOADING SEQUENCE HAS FINISHED
print ("Uploading sequence finished.")
quit()