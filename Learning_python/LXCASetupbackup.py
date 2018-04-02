from selenium import webdriver
import time, unittest, os
import webdriver as dr
from selenium.webdriver.common import action_chains, keys



class LxcaSetupTest(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        global condata
        condata = ['10.243.1.90', 'USERID', 'CME44len']
        inst.driver = dr.mycon()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        inst.driver.get('https://'+condata[0])

    def testula(self):
        try:
            self.driver.find_element_by_css_selector('#dijit__TemplatedMixin_1 > div:nth-child(2) > div:nth-child(3)').click()
            time.sleep(2)
            self.driver.find_element_by_css_selector('#lxca_coreUI_license_InitialSetupLicense_InitialSetupLicense_0_setupLicenseAcceptNode > span:nth-child(2)').click()#accept
        except:
            self.driver.find_element_by_xpath('//span/span[3][contains(text(),"Return to Initial Setup")]').click()
            time.sleep(2)
	#TODO: add assert

    def testCreateUser(self):
        self.driver.find_element_by_xpath('//div[3]/b[contains(text(),"Create User Account")]').click()#create user
	time.sleep(1)
	user1 = self.driver.find_element_by_id('lxca_customUI_security_usersManagement_usersManagementGrid_0usernameNode')
	pass1 = self.driver.find_element_by_id('lxca_customUI_security_usersManagement_usersManagementGrid_0newPassword')
	pass2 = self.driver.find_element_by_id('lxca_customUI_security_usersManagement_usersManagementGrid_0confirmPassword')
	
	user1.send_keys('USERID')
	pass1.send_keys(condata[1])
	pass2.send_keys(condata[1])
	time.sleep(.5)
	pass2.send_keys(keys.Keys.TAB,keys.Keys.ENTER)
	time.sleep(1)

	self.driver.find_element_by_css_selector('.dijitReset.dijitInline.dijitIcon.usersManagementToolIcon.usersManagementIconCreate').click()
	time.sleep(2)
	self.driver.find_element_by_id('lxca_customUI_security_usersManagement_usersManagementGrid_0usernameNode').send_keys('USER01')
	self.driver.find_element_by_id('lxca_customUI_security_usersManagement_usersManagementGrid_0newPassword').send_keys(condata[1])
	self.driver.find_element_by_id('lxca_customUI_security_usersManagement_usersManagementGrid_0confirmPassword').send_keys(condata[1])
	time.sleep(.5)
	self.driver.find_element_by_id('lxca_customUI_security_usersManagement_usersManagementGrid_0confirmPassword').send_keys(keys.Keys.TAB,keys.Keys.ENTER)
	time.sleep(1)
	#Return to setup
	self.driver.find_element_by_xpath('//span[3][contains(text(),"Return to Initial Setup")]').click()
	time.sleep(1)
	#TODO: Add assert

    def testNetworksettings(self):
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
        #TODO: Add assert
           
    def testSetServices(self):
        self.driver.find_element_by_xpath('//div[3]/b[contains(text(),"Configure Service And Support Settings")]').click()
	time.sleep(2)
	self.driver.find_element_by_id('dijit_form_RadioButton_0').click()
	time.sleep(2)
	self.driver.find_element_by_xpath('//div/span/span/span/span[3][contains(text(),"Apply")]').click()
	time.sleep(2)
	#TODO: Add assert

    def testParticapate(self):
        self.driver.find_element_by_id('dijit_form_RadioButton_1').click()
	time.sleep(2)
	self.driver.find_element_by_xpath('//div/span/span/span/span[3][contains(text(),"Apply")]').click()
	time.sleep(3)
	#TODO: Add assert


    def testCallhome(self):
        self.driver.find_element_by_xpath('//span[3][contains(text(),"Skip Step")]').click()
        time.sleep(2)
        #TODO: Add assert


    def testTbd(self):
        self.driver.find_element_by_xpath('//span/span[3][contains(text(),"Skip Step")]').click()
	time.sleep(2)
	#TODO: Add assert


    def testWarranty(self):
        time.sleep(2)
        self.driver.find_element_by_xpath('//span[3][contains(text(),"Skip Step")]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//span/span[contains(text(),"Return to Initial Setup")]').click()
        time.sleep(2)
        #TODO: Add assert

    def testSecuritysettings(self):
        self.driver.find_element_by_xpath('//div[3]/b[contains(text(),"Configure Additional Security Settings")]').click()
	time.sleep(1)
	self.driver.find_element_by_xpath('//div/span/span[contains(text(),"Account Security Settings")]').click()
	time.sleep(1)
	pasexp1 = self.driver.find_element_by_id('MaximumPasswordExpiration')
	paswarn1 = self.driver.find_element_by_id('PasswordExpirationWarningPeriod')
	pashis1 = self.driver.find_element_by_id('PasswordHistoryDepth')
	min1 = self.driver.find_element_by_id('MinimumChangeTime')
	maxfail1 = self.driver.find_element_by_id('MaximumLoginFailures')
	lockout1 = self.driver.find_element_by_id('LockoutTime')
	inac1 = self.driver.find_element_by_id('InactivityTimeout')

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
	#TODO: Add assert


    def testFinish(self):
        #start manage
	self.driver.find_element_by_xpath('//div[2]/div[3]/b[contains(text(),"Start Managing Systems")]').click()
	time.sleep(1)
	#no demo data
	self.driver.find_element_by_xpath('//span/span/span/span[3][contains(text(),"No")]').click()
	time.sleep(4)
	#TODO: Add assert



    @classmethod
    def tearDownClass(inst):
        inst.driver.quit()


if __name__ == '__main__':
    unittest.main()

	


        
