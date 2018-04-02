import unittest
from selenium import webdriver
import time, os, pyperclip
import LXCATaskTracker as jobtrack
from selenium.webdriver.common import action_chains, keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
global condata
condata = ['10.243.1.89', 'USERID', 'CME44len']


class ManageChassis(unittest.TestCase):
    
    @classmethod
    def setUpClass(inst):
        global condata
        condata = ['10.243.1.89', 'USERID', 'CME44len']

        # create a new Firefox session """
        inst.driver = webdriver.Firefox()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()

        inst.driver.get('https://'+condata[0]+'/')
        user = inst.driver.find_element_by_xpath('//input[contains(@placeholder,"user")]')
        paswd = inst.driver.find_element_by_xpath('//input[contains(@placeholder,"password")]')
        user.send_keys(condata[1])
        paswd.send_keys(condata[2])
        paswd.send_keys(keys.Keys.ENTER)
    def test_loggedin(self):
        #test = self.driver.find_element_by_xpath('//div[1][contains(@widgetid,"dashboard")][contains(@aria-label,"Dashboard")]')
        self.assertTrue(self.driver.find_element_by_xpath('//div[1][contains(@widgetid,"dashboard")][contains(@aria-label,"Dashboard")]').is_displayed())

    def test_Manage_Chassis(self):
        hw = self.driver.find_element_by_id('hardware')
        hw.click()
        disc = self.driver.find_element_by_id('dijit_MenuItem_18_text')
        disc.click()
        manInput = self.driver.find_element_by_xpath('//span[3][contains(@id,"manualInputBtn_label")]')
        manInput.click()
        time.sleep(5)
        self.assertTrue(self.driver.find_element_by_xpath('//label[contains(@id, "singleIPaddrId_label")]'))
        ipadd = self.driver.find_element_by_xpath('//input[contains(@id,"singleIPaddrId")]')
        ipadd.send_keys('10.243.0.23')
        ok1 = self.driver.find_element_by_xpath('//span[contains(@id,"manualIputDialog0_ok")][contains(@aria-disabled,"false")]')
        ok1.click()
        time.sleep(10)
        self.assertTrue(self.driver.find_element_by_xpath('//input[contains(@placeholder, "user name ( supervisor name)")]'))
        user1 = self.driver.find_element_by_xpath('//input[contains(@placeholder,"user name ( supervisor name)")]')
        user1.send_keys(condata[1])
        passwd1 = self.driver.find_element_by_xpath('//input[contains(@placeholder,"password")]')
        passwd1.send_keys(condata[2])
        recpw = self.driver.find_element_by_xpath('//input[contains(@placeholder,"RECOVERY_ID password")]')
        recpw.send_keys('IFM44test')
        recpwconfirm = self.driver.find_element_by_xpath('//input[contains(@placeholder,"confirm RECOVERY_ID password")]')
        recpwconfirm.send_keys('IFM44test')
        submit = self.driver.find_element_by_xpath('//span[3][contains(@id, "Dialog_submit_label")]')
        submit.click()
        time.sleep(2)
        self.assertTrue(self.driver.find_element_by_xpath('//span[contains(@id, "mgprocessDlg_title")]'))
        jobid = self.jobtrack.getjobid(condata)
        jobstatus = self.jobtrack.trackjob(condata, jobid)
        self.assertTrue(jobstatus == 'Complete')
        

    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()
