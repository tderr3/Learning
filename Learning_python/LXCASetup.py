from selenium import webdriver
import time, unittest, os, HtmlTestRunner, shutil
import driver
#import flexcatSetup
from selenium.webdriver.common import action_chains, keys



class lxcaSetupTest(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Firefox()
        inst.driver.implicitly_wait(5)
        inst.driver.maximize_window()
        inst.driver.get('https://10.243.1.100')
        #for file in os.listdir('c:\\python34\\Html_results\\'):
            #os.remove('c:\\python34\\Html_results\\'+file)
        '''user = inst.driver.find_element_by_xpath('//input[contains(@placeholder,"user")]')
        paswd = inst.driver.find_element_by_xpath('//input[contains(@placeholder,"password")]')
        user.send_keys('USERID')
        paswd.send_keys('CME44len')
        paswd.send_keys(keys.Keys.ENTER)'''

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
        '''
        self.driver.find_element_by_id('lxca_customUI_security_usersManagement_usersManagementGrid_0usernameNode').send_keys('USER01')
        self.driver.find_element_by_id('lxca_customUI_security_usersManagement_usersManagementGrid_0newPassword').send_keys('CME44len')
        self.driver.find_element_by_id('lxca_customUI_security_usersManagement_usersManagementGrid_0confirmPassword').send_keys('CME44len')'''
        time.sleep(.5)
        self.driver.find_element_by_xpath('//span[3][contains(text(),"Create")][contains(@id,"submitButtonForm")]').click()
        time.sleep(2)
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
        self.driver.find_element_by_xpath('//span[3][contains(text(), "Cancel")]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//span/span[3][contains(text(),"Return to Initial Setup")]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//span[3][contains(text(),"Close")]').click()#warning
        time.sleep(2)
        time.sleep(15)
        
        self.assertTrue(self.driver.find_element_by_xpath('//div[1][contains(@class,"floatLeft setupNetworkAccess completed")]'))
        
    def test_004_ntp(self):
        self.driver.find_element_by_xpath('//div[3]/b[contains(text(),"Configure Date and Time Preferences")]').click()
        time.sleep(4)
        self.driver.find_element_by_xpath('//div/span[1]/span/span/span[3][contains(text(),"Save")]').click()
        time.sleep(3)
        self.assertTrue(self.driver.find_element_by_xpath('//div[1][contains(@class,"setupDateAndTime completed")]'))
           
    def test_005_setServices(self):
        self.driver.find_element_by_xpath('//div[1][contains(@class, "setupServiceAndSupport")]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//span[contains(text(),"Usage Data")]').click()
        
        self.driver.find_element_by_xpath('//input[contains(@name,"feedBackRadioOptions")][contains(@value,"no")]').click()
        time.sleep(2)
        
        self.driver.find_element_by_xpath('//span[3][contains(text(),"Apply")]').click()
        time.sleep(2)

        self.assertEqual(self.driver.find_element_by_xpath('//div[1][contains(@widgetid,"workAreaHeader")]'),'Call Home Configuration')
        
        
        #self.assertTrue(self.driver.find_element_by_xpath('//div[1][contains(@class,"floatLeft setupDateAndself.time completed")]'))

    def test_006_Particapate(self):
        self.driver.find_element_by_id('dijit_form_RadioButton_1').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//div/span/span/span/span[3][contains(text(),"Apply")]').click()
        time.sleep(3)
        #TODO: Add assert
        self.assertTrue(self.driver.find_element_by_xpath('//div[1][contains(@class,"floatLeft setupUserAccount completed")]'))


    def test_007_Callhome(self):
        self.driver.find_element_by_xpath('//span[3][contains(text(),"Skip Step")]').click()
        time.sleep(2)
        #TODO: Add assert


    def test_008_Tbd(self):
        self.driver.find_element_by_xpath('//span/span[3][contains(text(),"Skip Step")]').click()
        time.sleep(2)
        #TODO: Add assert


    def test_009_Warranty(self):
        time.sleep(2)
        self.driver.find_element_by_xpath('//span[3][contains(text(),"Skip Step")]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//div[contains(text(),"Return to Initial Setup")]').click()
        time.sleep(2)
        #TODO: Add assert

    '''def test_010_Securitysettings(self):
        self.driver.find_element_by_xpath('//div[3]/b[contains(text(),"Configure Additional Security Settings")]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//div/span/span[contains(text(),"Account Security Settings")]').click()
        time.sleep(1)
        pasexp1 = self.driver.find_element_by_id('MaximumPasswordExpiration')
        paswarn1 = self.driver.find_element_by_id('PasswordExpirationWarningPeriod')
        pashis1 = self.driver.find_element_by_id('PasswordHistoryDepth')
        min1 = self.driver.find_element_by_id('MinimumChangeself.time')
        maxfail1 = self.driver.find_element_by_id('MaximumLoginFailures')
        lockout1 = self.driver.find_element_by_id('Lockoutself.time')
        inac1 = self.driver.find_element_by_id('Inactivityself.timeout')

        pasexp1.clear()
        paswarn1.clear()
        pashis1.clear()
        min1.clear()
        maxfail1.clear()
        lockout1.clear()
        inac1.clear()
        time.sleep(.5)


        pasexp1.send_keys('0')
        paswarn1.send_keys('0')
        pashis1.send_keys('0')
        min1.send_keys('0')
        maxfail1.send_keys('0')
        lockout1.send_keys('0')
        inac1.send_keys('0')
        time.sleep(.5)
        self.driver.find_element_by_id('saveAccountSecuritySettings_label').click()
        time.sleep(1.5)
        self.driver.find_element_by_xpath('//span/span/span/span[3][contains(text(),"Close")]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//div/div/span/span[contains(text(),"Return to Initial Setup")]').click()
        time.sleep(1.5)
        #TODO: Add assert'''


    def test_011_Finish(self):
        #start manage
        self.driver.find_element_by_xpath('//div[2]/div[3]/b[contains(text(),"Start Managing Systems")]').click()
        time.sleep(1)
        #no demo data
        self.driver.find_element_by_xpath('//span/span/span/span[3][contains(text(),"No")]').click()
        time.sleep(4)
        #TODO: Add assert'''



    @classmethod
    def tearDownClass(inst):
        flexcatSetup.both('10.243.1.100')
        inst.driver.quit()

    def isDisplayed(self,elems):
        for element in elems:
            if element.is_displayed() == True:
                return element


if __name__ == '__main__':
    #unittest.main(verbosity=2)
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='c:\\python34\\Html_results\\'))

        


        
