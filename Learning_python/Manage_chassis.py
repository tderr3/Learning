import unittest
import HtmlTestRunner
from selenium import webdriver
import time, os, pyperclip
import LXCATaskTracker as jobtrack
import webdriver as dr
from selenium.webdriver.common import action_chains, keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
global condata
condata = ['10.243.1.90', 'USERID', 'CME44len']
jobtrack.warnings.filterwarnings('ignore')

class test_002_ManageChassisTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(inst):
        global condata
        condata = ['10.243.1.90', 'USERID', 'CME44len']

        # create a new Firefox session """
        #inst.driver = webdriver.Firefox()
        inst.driver = dr.mycon()
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
        disc = self.driver.find_element_by_xpath('//td[contains(text(),"Discover and Manage New Devices")]')
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
        time.sleep(2)
        passwd1 = self.driver.find_element_by_xpath('//input[contains(@placeholder,"password")][contains(@id,"chassisPasswordId")]')
        passwd1.send_keys(condata[2])
        time.sleep(2)
        recpw = self.driver.find_element_by_xpath('//input[contains(@placeholder,"RECOVERY_ID password")][contains(@id,"LoginDialogpassword1")][not(contains(@id,"Rack"))]')
        recpw.send_keys('IFM44test')
        time.sleep(2)
        recpwconfirm = self.driver.find_element_by_xpath('//input[contains(@placeholder,"confirm RECOVERY_ID password")][contains(@id,"LoginDialogpassword2")][not(contains(@id,"Rack"))]')
        recpwconfirm.send_keys('IFM44test')
        time.sleep(2)
        submit = self.driver.find_element_by_xpath('//span[3][contains(@id, "Dialog_submit_label")]')
        submit.click()
        time.sleep(5)
        self.assertTrue(self.driver.find_element_by_xpath('//span[contains(@id, "mgprocessDlg_title")]'))
        jobid = jobtrack.getjobid(condata)
        jobstatus = jobtrack.trackjob(condata, jobid)
        self.assertTrue(jobstatus == 'Complete')
        

    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()

'''class test_001_lxcaSetupTest(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        #global condata
        #condata = ['10.243.1.90', 'USERID', 'CME44len']
        inst.driver = webdriver.Firefox()
        inst.driver.implicitly_wait(5)
        inst.driver.maximize_window()
        inst.driver.get('https://10.243.1.90')
        user = inst.driver.find_element_by_xpath('//input[contains(@placeholder,"user")]')
        paswd = inst.driver.find_element_by_xpath('//input[contains(@placeholder,"password")]')
        user.send_keys('USERID')
        paswd.send_keys('CME44len')
        paswd.send_keys(keys.Keys.ENTER)

    def test_001_Ula(self):
        self.driver.find_element_by_xpath('//b[contains(text(),"Read and Accept Lenovo® XClarity Administrator License Agreement")]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//span[3][contains(text(),"Accept")]').click()#accept
        
        #self.driver.find_element_by_xpath('//span/span[3][contains(text(),"Return to Initial Setup")]').click()
        time.sleep(2)
        self.assertTrue(self.driver.find_element_by_xpath('//div[1][contains(@class, "floatLeft setupLicense completed")]'))
        time.sleep(2)

    def test_002_CreateUser(self):
        self.driver.find_element_by_xpath('//b[contains(text(),"Create User Account")]').click()#create user
        time.sleep(1)
        user1 = self.driver.find_element_by_xpath('//input[contains(@placeholder,"Username")]')
        pass1 = self.driver.find_element_by_xpath('//input[contains(@placeholder,"New password")]')
        pass2 = self.driver.find_element_by_xpath('//input[contains(@id , "confirmPassword")]')
        
        user1.send_keys('USERID')
        pass1.send_keys('CME44len')
        pass2.send_keys('CME44len')
        time.sleep(.5)
        self.driver.find_element_by_xpath('//span[3][contains(text(),"Create")][contains(@id,"submitButtonForm")]').click()
        time.sleep(1)
        self.assertTrue(self.driver.find_element_by_xpath('//td[1][contains(text(),"USERID")]'))

        self.driver.find_element_by_xpath('//span[contains(@title,"Create New User")]').click()
        time.sleep(2)
        user1 = self.driver.find_element_by_xpath('//input[contains(@placeholder,"Username")]')
        pass1 = self.driver.find_element_by_xpath('//input[contains(@placeholder,"New password")]')
        pass2 = self.driver.find_element_by_xpath('//input[contains(@id , "confirmPassword")]')
        user1.send_keys('USER01')
        pass1.send_keys('CME44len')
        pass2.send_keys('CME44len')
        
        self.driver.find_element_by_id('lxca_customUI_security_usersManagement_usersManagementGrid_0usernameNode').send_keys('USER01')
        self.driver.find_element_by_id('lxca_customUI_security_usersManagement_usersManagementGrid_0newPassword').send_keys('CME44len')
        self.driver.find_element_by_id('lxca_customUI_security_usersManagement_usersManagementGrid_0confirmPassword').send_keys('CME44len')
        time.sleep(.5)
        self.driver.find_element_by_xpath('//span[3][contains(text(),"Create")][contains(@id,"submitButtonForm")]').click()
        time.sleep(1)
        self.assertTrue(self.driver.find_element_by_xpath('//td[1][contains(text(),"USER01")]'))
        #Return to setup
        self.driver.find_element_by_xpath('//span[3][contains(text(),"Return to Initial Setup")]').click()
        time.sleep(1)
        
        self.assertTrue(self.driver.find_element_by_xpath('//div[1][contains(@class,"floatLeft setupUserAccount completed")]'))

    def test_003_Networksettings(self):
        time.sleep(2)
        self.driver.find_element_by_xpath('//div[3]/b[contains(text(),"Configure Network Access")]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//span/span[contains(text(),"discover and manage hardware only.")]').click()
        time.sleep(.5)
        self.driver.find_element_by_xpath('//table/tbody/tr[1]/td[2][contains(text(),"images")]').click()
        time.sleep(.5)
        #save ip settings
        self.driver.find_element_by_xpath('//span/span/span[3][contains(text(),"Save IP Settings")]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//span[2]/span[1]/span/span/span[3][contains(text(),"Save")]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//div[2]/div[1]/div[2]/a[contains(text(), "Show Details")]').send_keys(keys.Keys.TAB,keys.Keys.TAB,keys.Keys.TAB,keys.Keys.ENTER)
        time.sleep(2)
        self.driver.find_element_by_xpath('//span/span[3][contains(text(),"Return to Initial Setup")]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//div[4]/span[3]/span/span/span/span[3][contains(text(),"Close")]').click()#warning
        time.sleep(2)
        
        self.assertTrue(self.driver.find_element_by_xpath('//div[1][contains(@class,"floatLeft setupNetworkAccess completed")]'))
        
    def test_004_ntp(self):
        self.driver.find_element_by_xpath('//div[3]/b[contains(text(),"Configure Date and Time Preferences")]').click()
        time.sleep(4)
        self.driver.find_element_by_xpath('//div/span[1]/span/span/span[3][contains(text(),"Save")]').click()
        time.sleep(3)
        self.assertTrue(self.driver.find_element_by_xpath('//div[1][contains(@class,"setupDateAndTime completed")]'))


    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()'''



if __name__ == '__main__':
    #unittest.main(verbosity=3)
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='c:\\python34\\Html_results\\'))
