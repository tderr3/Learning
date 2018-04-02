from selenium import webdriver
import time
import os
from selenium.webdriver.common import action_chains, keys

#print('LXCA IP address?')
#lxcaIp = input()
#lxcaIp = '10.243.1.89'
#lxcaIp = '10.243.13.181'
#lxcaIp = 'https://'+ lxcaIp



def mycon():
	spam1 = webdriver.Firefox(webdriver.FirefoxProfile(os.path.normpath('c:/Automation_web/ffprofile/')))
	return spam1


def login(spam, condata):
	spam.find_element_by_id('idx_form_TextBox_0').send_keys('USERID')
	spam.find_element_by_id('augusta-login-framePassword').send_keys(condata[1])
	spam.find_element_by_xpath('//span[1]/span/span/span[3][contains(text(),"Log In")]').click()
	time.sleep(2)


def lice(spam):
	try:
		spam.find_element_by_css_selector('#dijit__TemplatedMixin_1 > div:nth-child(2) > div:nth-child(3)').click()#licecne
		time.sleep(2)
		spam.find_element_by_css_selector('#lxca_coreUI_license_InitialSetupLicense_InitialSetupLicense_0_setupLicenseAcceptNode > span:nth-child(2)').click()#accept
	except:
		spam.find_element_by_xpath('//span/span[3][contains(text(),"Return to Initial Setup")]').click()
		time.sleep(2)

def createuser(spam, condata):
	spam.find_element_by_xpath('//div[3]/b[contains(text(),"Create User Account")]').click()#create user
	time.sleep(1)
	user1 = spam.find_element_by_id('lxca_customUI_security_usersManagement_usersManagementGrid_0usernameNode')
	pass1 = spam.find_element_by_id('lxca_customUI_security_usersManagement_usersManagementGrid_0newPassword')
	pass2 = spam.find_element_by_id('lxca_customUI_security_usersManagement_usersManagementGrid_0confirmPassword')
	
	user1.send_keys('USERID')
	pass1.send_keys(condata[1])
	pass2.send_keys(condata[1])
	time.sleep(.5)
	pass2.send_keys(keys.Keys.TAB,keys.Keys.ENTER)
	time.sleep(1)

	spam.find_element_by_css_selector('.dijitReset.dijitInline.dijitIcon.usersManagementToolIcon.usersManagementIconCreate').click()
	time.sleep(2)
	spam.find_element_by_id('lxca_customUI_security_usersManagement_usersManagementGrid_0usernameNode').send_keys('USER01')
	spam.find_element_by_id('lxca_customUI_security_usersManagement_usersManagementGrid_0newPassword').send_keys(condata[1])
	spam.find_element_by_id('lxca_customUI_security_usersManagement_usersManagementGrid_0confirmPassword').send_keys(condata[1])
	time.sleep(.5)
	spam.find_element_by_id('lxca_customUI_security_usersManagement_usersManagementGrid_0confirmPassword').send_keys(keys.Keys.TAB,keys.Keys.ENTER)
	time.sleep(1)
	#Return to setup
	spam.find_element_by_xpath('//span[3][contains(text(),"Return to Initial Setup")]').click()
	time.sleep(1)

def netconfig(spam):


#Configure Network access
	time.sleep(2)
	spam.find_element_by_xpath('//div[3]/b[contains(text(),"Configure Network Access")]').click()
	time.sleep(2)
	spam.find_element_by_xpath('//span/span[contains(text(),"discover and manage hardware only.")]').click()
	time.sleep(.5)
	spam.find_element_by_xpath('//table/tbody/tr[1]/td[2][contains(text(),"images")]').click()
	time.sleep(.5)
	#save ip settings
	spam.find_element_by_xpath('//span/span/span[3][contains(text(),"Save IP Settings")]').click()
	time.sleep(2)
	spam.find_element_by_xpath('//span[2]/span[1]/span/span/span[3][contains(text(),"Save")]').click()
	time.sleep(2)
	spam.find_element_by_xpath('//div[2]/div[1]/div[2]/a[contains(text(), "Show Details")]').send_keys(keys.Keys.TAB,keys.Keys.TAB,keys.Keys.TAB,keys.Keys.ENTER)
	time.sleep(2)
	spam.find_element_by_xpath('//span/span[3][contains(text(),"Return to Initial Setup")]').click()
	time.sleep(2)
	spam.find_element_by_xpath('//div[4]/span[3]/span/span/span/span[3][contains(text(),"Close")]').click()#warning
	time.sleep(2)

def ntp(spam):
	spam.find_element_by_xpath('//div[3]/b[contains(text(),"Configure Date and Time Preferences")]').click()
	time.sleep(2)
	spam.find_element_by_xpath('//div/span[1]/span/span/span[3][contains(text(),"Save")]').click()
	time.sleep(4)

#Configure Service
def Setservices(spam):
	spam.find_element_by_xpath('//div[3]/b[contains(text(),"Configure Service And Support Settings")]').click()
	time.sleep(2)
	spam.find_element_by_id('dijit_form_RadioButton_0').click()
	time.sleep(2)
	spam.find_element_by_xpath('//div/span/span/span/span[3][contains(text(),"Apply")]').click()
	time.sleep(2)

def partic(spam):
	spam.find_element_by_id('dijit_form_RadioButton_1').click()
	time.sleep(2)
	spam.find_element_by_xpath('//div/span/span/span/span[3][contains(text(),"Apply")]').click()
	time.sleep(3)

def callhome(spam):
        spam.find_element_by_xpath('//span[3][contains(text(),"Skip Step")]').click()
        time.sleep(2)
       
        

def what(spam):
	spam.find_element_by_xpath('//span/span[3][contains(text(),"Skip Step")]').click()
	time.sleep(2)
	#spam.find_element_by_xpath('//a/div/div/span/span[contains(text(),"Return to Initial Setup")]').click()
	#time.sleep(2)
	
def warranty(spam):
        time.sleep(2)
        spam.find_element_by_xpath('//span[3][contains(text(),"Skip Step")]').click()
        time.sleep(2)
        spam.find_element_by_xpath('//span/span[contains(text(),"Return to Initial Setup")]').click()
        time.sleep(2)

def services(spam):
	Setservices(spam)
	partic(spam)
	callhome(spam)
	what(spam)
	warranty(spam)

def security(spam):
	spam.find_element_by_xpath('//div[3]/b[contains(text(),"Configure Additional Security Settings")]').click()
	time.sleep(1)
	spam.find_element_by_xpath('//div/span/span[contains(text(),"Account Security Settings")]').click()
	time.sleep(1)
	pasexp1 = spam.find_element_by_id('MaximumPasswordExpiration')
	paswarn1 = spam.find_element_by_id('PasswordExpirationWarningPeriod')
	pashis1 = spam.find_element_by_id('PasswordHistoryDepth')
	min1 = spam.find_element_by_id('MinimumChangeTime')
	maxfail1 = spam.find_element_by_id('MaximumLoginFailures')
	lockout1 = spam.find_element_by_id('LockoutTime')
	inac1 = spam.find_element_by_id('InactivityTimeout')

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
	spam.find_element_by_id('saveAccountSecuritySettings_label').click()
	time.sleep(1.5)
	spam.find_element_by_xpath('//span/span/span/span[3][contains(text(),"Close")]').click()
	time.sleep(1)
	spam.find_element_by_xpath('//div/div/span/span[contains(text(),"Return to Initial Setup")]').click()
	time.sleep(1.5)

def setglobalpw(driver):
	driver.find_element_by_id('provisioning').click()
	time.sleep(.5)
	driver.find_element_by_link_text('Deploy OS Images').click()
	time.sleep(5)
	driver.find_element_by_xpath('//span[1][contains(@class,"dijitReset dijitInline dijitIcon flexCatGlobalSettingsIcon")]').click()
	time.sleep(2)
	driver.find_element_by_xpath('//div/input[contains(@id,"linuxPasswordBox")]').send_keys('CME44len')
	time.sleep(.5)
	driver.find_element_by_xpath('//div/input[contains(@id,"linuxConfirmPwdBox")]').send_keys('CME44len')
	time.sleep(.5)
	driver.find_element_by_xpath('//div/input[contains(@id,"windowsPasswordBox")]').send_keys('CME44len')
	time.sleep(.5)
	driver.find_element_by_xpath('//div/input[contains(@id,"windowsConfirmPwdBox")]').send_keys('CME44len')
	time.sleep(1)
	driver.find_element_by_xpath('//span[contains(@id,"globalSettingOKBtn")][contains(@role,"button")]').click()
	time.sleep(5)


def finish(spam):
	#start manage
	spam.find_element_by_xpath('//div[2]/div[3]/b[contains(text(),"Start Managing Systems")]').click()
	time.sleep(1)
	#no demo data
	spam.find_element_by_xpath('//span/span/span/span[3][contains(text(),"No")]').click()
	time.sleep(4)
	spam.quit()

def manageChassis(spam, ip):
	try:
		spam.find_element_by_xpath('//div[1][contains(@id,"workAreaHeader")][contains(text(),"Discover and Manage New Devices")]')
	except:
		spam.find_element_by_id('Hardware').click()
		spam.find_element_by_xpath('//td[2][contains(text(),"Discover and Manage New")]').click()
	spam.find_element_by_xpath('//span[3][contains(@id,"manualInputBtn")]').click()
	spam.find_element_by_xpath('//div[1]/div/input[contains(@id,"manualIputDialog")][contains(@name,"singleOrMultipleAssignId")]').send_keys('10.243.0.23')
	
	
	
	
'''spam = mycon()
spam.implicitly_wait(15)
spam.get(lxcaIp)
time.sleep(5)

spam.maximize_window()	
lice(spam)
createuser(spam)
netconfig(spam)
ntp(spam)
services(spam)
security(spam)
finish(spam)'''






