import unittest
from selenium import webdriver
import time, os
from selenium.webdriver.common import keys

class managechassis(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('https://10.243.1.90')

    def login(self):
        user = self.driver.find_element_by_xpath('//input[contains(@placeholder,"user")]')
        pas = self.driver.find_element_by_xpath('//input[contains(@placeholder,"password")]')
        self.user.send_keys('USERID')
        self.pas.send_keys('CME44len')
        self.pas.send_keys(keys.Keys.ENTER)
        test = self.driver.find_element_by_xpath('//div[1][contains(@widgetid,"dashboard")][contains(@aria-label,"Dashboard")]')
        self.assertTrue(test.aria-label, "Dashboard")
        

    #@classmethod
    def tearDown(self):
        self.driver.quit()

if __name__=='_main__':
    unittest.main()
