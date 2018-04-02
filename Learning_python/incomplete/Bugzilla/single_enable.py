#! python3
from selenium import webdriver
import sys, time

prod = sys.argv[1]
rel = sys.argv[2]

def mycon():
    profile = webdriver.FirefoxProfile(z)
    profile.accept_untrusted_certs = True
    driver = webdriver.Firefox(profile)
    return driver

def disable_rel(driver, prod, rel):
    try:

        driver.get(r'https://bz-test.labs.lenovo.com/editversions.cgi?action=edit&product='+prod+'&version='+rel)
        time.sleep(.5)
        ckbox = driver.find_element_by_xpath('//input[contains(@id,"isactive")]')
        save= driver.find_element_by_xpath('//input[5][contains(@id,"update")]')
        if ckbox.get_attribute('checked') != 'true':
            ckbox.click()
            save.click()
            print(rel+' Activated for '+prod)
            time.sleep(.5)
            
        else:
            print('Release is already enabled for '+prod)
            #save.click()
            time.sleep(.5)
    except:
           
        print(prod + ' and ' +Rel +' does not compute')
        continue

driver = mycon()

disable_rel(driver, prod, rel)
