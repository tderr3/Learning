import unittest, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class CPtesting(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        


    def test_login_in_to_lxca_org(self):
        driver = self.driver
        driver.get("https://10.243.1.90")
        username = driver.find_element_by_id('idx_form_TextBox_0')
        username.send_keys("USERID")
        password= driver.find_element_by_id('augusta-login-framePassword')
        password.send_keys("CME44len")
        loginbutton=driver.find_element_by_xpath('//span[1]/span/span/span[3][contains(text(),"Log In")]')
        loginbutton.click()
        time.sleep(2)
        prov = driver.find_element_by_id('provisioning')
        prov.click()
        patterns = driver.find_element_by_link_text('Patterns')
        patterns.click()
        time.sleep(2)
        header = driver.find_element_by_id('workAreaHeader')
        self.assertEqual(header.text, 'Configuration Patterns: Patterns')
        prov = driver.find_element_by_id('provisioning')
        prov.click()
        manage = driver.find_element_by_link_text('Manage OS Images')
        manage.click()
        time.sleep(2)
        header = driver.find_element_by_id('workAreaHeader')
        self.assertEqual(header.text,'Deploy Operating Systems: Manage OS Images')




    '''def test1(self):
        
        prov = driver.find_element_by_id('provisioning')
        prov.click()
        manage = driver.find_element_by_link_text('Manage OS Images')
        manage.click()
        time.sleep(2)
        header = driver.find_element_by_id('workAreaHeader')
        self.assertEqual(header.text,'Deploy Operating Systems: Manage OS Images')'''
        
        
        

    

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
