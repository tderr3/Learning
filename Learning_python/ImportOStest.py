from selenium import webdriver
import time, unittest, os, HtmlTestRunner
import webdriver as dr
import flexcatSetup
from selenium.webdriver.common import action_chains, keys
import LXCATaskTracker as jobtrack
jobtrack.warnings.filterwarnings('ignore')

class test_003_importOS(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        global condata
        condata = ['10.243.1.90', 'USERID', 'CME44len']
        
        inst.driver = webdriver.Firefox()
        inst.driver.implicitly_wait(5)
        inst.driver.maximize_window()
        inst.driver.get('https://'+ condata[0])
        user = inst.driver.find_element_by_xpath('//input[contains(@placeholder,"user")]')
        paswd = inst.driver.find_element_by_xpath('//input[contains(@placeholder,"password")]')
        user.send_keys('USERID')
        paswd.send_keys('CME44len')
        paswd.send_keys(keys.Keys.ENTER)
        time.sleep(2)


    def test_001(self):
        prov = self.driver.find_element_by_id('provisioning')
        prov.click()
        time.sleep(3)
        manOSImages = self.driver.find_element_by_link_text('Manage OS Images')
        manOSImages.click()
        time.sleep(2)
        importOSimagebutton = self.driver.find_element_by_xpath('//span[contains(@id, "importOSBtn")][contains(@class, "ButtonContents")][contains(@aria-disabled,"false")]')
        importOSimagebutton.click()
        time.sleep(1)
        remoteTab = self.driver.find_element_by_xpath('//span[2][contains(text(),"Remote Import")]')
        remoteTab.click()
        pathToFile = self.driver.find_element_by_xpath('//input[contains(@placeholder,"example: /isos/VMWare/6.0u1/LNV2016.iso")]')
        pathToFile.send_keys('/images/ESXI/ESXI6-0.iso')
        elements = self.driver.find_elements_by_xpath('//span[contains(@aria-checked,"false")][contains(@class,"SelectionCheckBox")]')
        remoteServer = self.isDisplayed(elements)
        remoteServer.click()
        elements = self.driver.find_elements_by_xpath('//span[3][contains(text(),"Import")][contains(@id,"importButton_label")]')
        importButton = self.isDisplayed(elements)
        self.assertTrue(importButton.is_displayed())
        importButton.click()
        time.sleep(3)
        jobid = jobtrack.getjobid(condata)
        jobstatus = jobtrack.trackjob(condata, jobid)
        self.assertTrue(jobstatus == 'Complete')



    '''def isDisplayed(self,elems):
        for element in elems:
            if element.is_displayed() == True:
                return element'''
                
    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()

    def isDisplayed(self,elems):
        for element in elems:
            if element.is_displayed() == True:
                return element


if __name__ == '__main__':
    #unittest.main(verbosity=3)
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='c:\\python34\\Html_results\\'))     
        
