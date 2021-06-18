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
# example of adding options


driver = webdriver.Chrome(executable_path="D:\Academic_Software\Eclipse\python\chromedriver.exe")

url = "https://www.doctolib.de/praxis/muenchen/hausarztpraxis-dr-grassl?utm_medium=referral&utm_campaign=website-button&utm_content=option-5&utm_term=hausarztpraxis-dr-grassl&utm_source=hausarztpraxis-dr-grassl-website-button"
driver.get(url)

#see if this finds the right button
time.sleep(3)

python_button = "//*[@id='didomi-notice-disagree-button']"
driver.find_element_by_xpath(python_button).click()


#python_button[0].click()