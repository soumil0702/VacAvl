'''
Created on 18 Jun 2021

@author: soumi
'''

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time
import sys

#import win32api
import winsound
# example of adding options

#PRINT SYNTAX print("Total students : %3d, Boys : %2d" % (240, 120))

driver = webdriver.Chrome(executable_path="D:\Academic_Software\Eclipse\python\chromedriver.exe")

url_pfizer =[ "https://www.doctolib.de/praxis/muenchen/hausarztpraxis-dr-grassl?utm_medium=referral&utm_campaign=website-button&utm_content=option-5&utm_term=hausarztpraxis-dr-grassl&utm_source=hausarztpraxis-dr-grassl-website-button",
      "https://termin.dachau-med.de/impfungen03/"]

grassl="https://www.doctolib.de/praxis/muenchen/hausarztpraxis-dr-grassl?utm_medium=referral&utm_campaign=website-button&utm_content=option-5&utm_term=hausarztpraxis-dr-grassl&utm_source=hausarztpraxis-dr-grassl-website-button"
dachau="https://termin.dachau-med.de/impfungen03/"
#see if this finds the right button
time.sleep(2)

while True:
    try:
        driver.get(grassl)
        cookiesBtn = "//*[@id='didomi-notice-disagree-button']"
        if(driver.find_elements_by_xpath(cookiesBtn)):
            driver.find_element_by_xpath(cookiesBtn).click()
        driver.find_element_by_xpath("//*[@id='booking_speciality']/option[3]").click()
        driver.find_element_by_xpath("//*[@id='booking_insurance_sector']/option[1]").click()
        pfizer="//*[@id='booking_motive']/option[2]";
        astra="//*[@id='booking_motive']/option[3]"
        
        driver.find_element_by_xpath(pfizer).click()
        
        #driver.find_element_by_xpath(astra).click()
        time.sleep(1)
        x=driver.find_elements_by_class_name("booking-message") #see if warning is available#

        if(not x): #change this to not x
            print(x)
            print("Hallelujah!!!!! Grassl Vaccine available at ")
            winsound.Beep(3000,7000)
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            print("At time ",current_time)
            break;
        time.sleep(1)

    except Exception as e:
        print(e)
        sys.exit()
    
#python_button[0].click()