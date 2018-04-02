#! python3

from selenium import webdriver
from selenium.webdriver.common import action_chains, keys
import os, sys, time, pyperclip

cp = pyperclip.paste()
product_list= cp.split('\r\n')
product_list.remove('')
#release = sys.argv[1]


release = 'Async OS Bus - Windows Nano RS3 (Dec 2017)'#input release to deactivate here



def mycon():
    profile = webdriver.FirefoxProfile(os.path.normpath('c:/Automation_web/ffprofile/'))
    profile.accept_untrusted_certs = True
    driver = webdriver.Firefox(profile)
    return driver

def disable_rel(driver, plist, rel):
    for product in plist:
        try:

            driver.get(r'https://bz-test.labs.lenovo.com/editversions.cgi?action=edit&product='+product+'&version='+rel)
            time.sleep(.5)
            #todo add logic to check for error message due to product or release does not exist

        
            ckbox = driver.find_element_by_xpath('//input[contains(@id,"isactive")]')
            save= driver.find_element_by_xpath('//input[5][contains(@id,"update")]')
            if ckbox.get_attribute('checked') == 'true':
                ckbox.click()
                save.click()
                print(rel+' Deactivated for '+product)
                time.sleep(.5)
            
            else:
                print('Release is already disabled for '+product)
                #save.click()
                time.sleep(.5)
        except:
           
            print('Product or Release is wrong please check ' + product)
            continue
    
        


    
    
    



driver = mycon()
disable_rel(driver, product_list, release)

