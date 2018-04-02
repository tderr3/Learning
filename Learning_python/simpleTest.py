import unittest
from selenium import webdriver
import driver, os, paramiko, time, sys, HtmlTestRunner, random
#from ifm_bvt import *



class simple_test(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.dr = driver.mycon()
        inst.dr.implicitly_wait(20)
        inst.dr.maximize_window()
        inst.dr.get('http://toolsqa.com/automation-practice-form/')
        time.sleep(3)

    def test_001_test_1(self):
        self.assertTrue(self.dr.find_element_by_partial_link_text('Partial Link Test').is_displayed())


    def test_002_test_2(self):
        self.assertTrue(self.dr.find_element_by_xpath('//input[contains(@name, "firstname")]').is_displayed())


    def test_003_test_3(self):
        self.assertTrue(self.dr.find_element_by_xpath('//input[contains(@name, "lastname")]').is_displayed())


    def test_004_test_4(self):
        self.assertTrue(self.dr.find_element_by_id('exp-0').is_displayed())

        

    @classmethod
    def tearDownClass(inst):
        inst.dr.quit()



if __name__ == '__main__':
    #unittest.main(verbosity=3)
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='c:\\python34\\Html_results\\',template='c:\\python34\\testReport.html', report_title='My Report' ))

