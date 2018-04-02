#! python3

from selenium import webdriver
import time
import os
import sys


condata=[sys.argv[1],sys.argv[2],sys.argv[3]]

def mycon():
	driver1 = webdriver.Firefox(webdriver.FirefoxProfile(os.path.normpath('c:/Automation_web/ffprofile/')))
	return driver1


def login(driver, coninfo):
	driver.find_element_by_id('idx_form_TextBox_0').send_keys(coninfo[1])
	time.sleep(1)
	driver.find_element_by_id('augusta-login-framePassword').send_keys(coninfo[2])
	time.sleep(1)
	driver.find_element_by_xpath('//span[1]/span/span/span[3][contains(text(),"Log In")]').click()
	time.sleep(2)

driver = mycon()

driver.get('https://'+condata[0])
driver.maximize_window()

time.sleep(5)
try:
    login(driver, condata)
    sys.exit
except Exception as ex:
    print(ex)

    

