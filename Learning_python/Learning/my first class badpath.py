import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class DemoMaharaOrgLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login_in_demo_mahara_org(self):
        driver = self.driver
        #driver.get("http://demo.mahara.org/")
        driver.get("https://10.243.1.89")
        self.assertIn('bad data', driver.title)
        username = driver.find_element_by_id('idx_form_TextBox_0')
        username.send_keys("USERID")
        password= driver.find_element_by_id('augusta-login-framePassword')
        password.send_keys("CME44len")
        loginbutton=driver.find_element_by_xpath('//span[1]/span/span/span[3][contains(text(),"Log In")]')
        loginbutton.click()
        self.assertTrue(driver.title,'10.243.1.90 - Lenovo XClarity Administrator')
        #driver.'10.243.1.89 - Lenovo XClarity Administrator | Login'

    def tearDown(self):
        self.driver.close()


'''class DemoMaharaOrgLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_login_in_demo_mahara_org(self):
        driver = self.driver
        #driver.get("http://demo.mahara.org/")
        driver.get("https://10.243.1.89")
        self.assertIn('10.243.1.89 - Lenovo XClarity Administrator | Login', driver.title)
        username = driver.find_element_by_id('idx_form_TextBox_0')
        username.send_keys("USERID")
        password= driver.find_element_by_id('augusta-login-framePassword')
        password.send_keys("CME44len")
        loginbutton=driver.find_element_by_xpath('//span[1]/span/span/span[3][contains(text(),"Log In")]')
        loginbutton.click()
        self.assertTrue(driver.title,'10.243.1.90 - Lenovo XClarity Administrator')
        #driver.'10.243.1.89 - Lenovo XClarity Administrator | Login'

    def tearDown(self):
        self.driver.close()'''





if __name__ == "__main__":
    unittest.main()
