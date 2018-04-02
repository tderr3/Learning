from selenium import webdriver
import sys, time, os

prod = sys.argv[1]
rel = sys.argv[2]

def mycon():
    '''profile = webdriver.FirefoxProfile(os.path.normpath('/var/www/html/todd/ffprofile/test'))
    profile.accept_untrusted_certs = True
    driver = webdriver.Firefox(profile)
    return driver'''
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    #chrome_options.binary_location = '/



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

        print(prod + ' and ' +rel +' does not compute')

driver = mycon()

disable_rel(driver, prod, rel)
driver.quit()
