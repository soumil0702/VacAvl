'''
Created on 18 Jun 2021

@author: soumi
'''

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
import time
import sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#import win32api
import winsound
from conda_verify.cli import cli
from selenium.webdriver.support.wait import WebDriverWait
# example of adding options

#PRINT SYNTAX print("Total students : %3d, Boys : %2d" % (240, 120))

#driver = webdriver.Chrome(executable_path="D:\Academic_Software\Eclipse\python\chromedriver.exe")
driver = webdriver.Chrome(executable_path="E:\shared_bw_win7and10\Eclipse_Testing\chromedriver_win32\chromedriver.exe")
url_pfizer =[ "https://www.doctolib.de/praxis/muenchen/hausarztpraxis-dr-grassl?utm_medium=referral&utm_campaign=website-button&utm_content=option-5&utm_term=hausarztpraxis-dr-grassl&utm_source=hausarztpraxis-dr-grassl-website-button",
      "https://termin.dachau-med.de/impfungen03/"]

dachau="https://termin.dachau-med.de/impfungen03/"
#see if this finds the right button
time.sleep(2)



def scrapeGrassll(vacType): #0=pfizer, 1 = astra
    
    grassl="https://www.doctolib.de/praxis/muenchen/hausarztpraxis-dr-grassl?utm_medium=referral&utm_campaign=website-button&utm_content=option-5&utm_term=hausarztpraxis-dr-grassl&utm_source=hausarztpraxis-dr-grassl-website-button"

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
            
            if(vacType==0):
                vacType=pfizer
            elif(vacType==1):
                vacType=astra
            
            driver.find_element_by_xpath(vacType).click()
            
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
                driver.switch_to.window(driver.window_handles[0])


                break;
            time.sleep(1)
    
        except Exception as e:
            print(e)
            sys.exit()    
    
def scrapeDachau():
    driver.get(dachau)
    time.sleep(1)
    dropdownXpath="/html/body/span/span/span[2]/ul/li" #doesnt work for some reason
    driver.find_element_by_class_name("select2-selection--single").click()
    x=(driver.find_elements_by_xpath(dropdownXpath))
    driver.find_element_by_xpath('//*[@id="sln-step-submit"]').click()


    timeout = 5
    try:
        element_present = EC.presence_of_element_located((By.CLASS_NAME, 'sln-alert--problem'))
        WebDriverWait(driver, timeout).until(element_present)
        
        print("Page loaded")
    except TimeoutException:
        print("Timed out waiting for page to load")
 #   finally:
 #       print("Page loaded")
    
#     if (driver.find_elements_by_class_name("sln-alert--problem")):
#         print('found warning')
        

if __name__ == '__main__':
#     driver.get("https://www.reddit.com")
#     driver.execute_script("window.open()")
#     print(driver.window_handles)
#     driver.switch_to.window(driver.window_handles[1])
#     driver.get("https://www.youtube.com")
#     time.sleep(1)
#     driver.switch_to.window(driver.window_handles[0])
#     driver.get("https://python.org")
#    scrapeGrassll(0)
     scrapeDachau()  
#python_button[0].click()