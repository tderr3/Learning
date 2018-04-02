from selenium import webdriver
import time
import os
from selenium.webdriver.common import action_chains, keys
from jobgrab import getjobid, getjobstatus

#print('LXCA IP address?')
#lxcaIp = input()
#lxcaIp = '10.243.1.89'
#lxcaIp = '10.243.13.181'
#lxcaIp = 'https://'+ lxcaIp



def mycon():
	spam1 = webdriver.Firefox(webdriver.FirefoxProfile(os.path.normpath('c:/Automation_web/ffprofile/')))
	return spam1


def login(spam, condata):
	time.sleep(1)
	spam.find_element_by_id('idx_form_TextBox_0').send_keys(condata[1])
	spam.find_element_by_id('augusta-login-framePassword').send_keys(condata[2])
	spam.find_element_by_xpath('//span[1]/span/span/span[3][contains(text(),"Log In")]').click()
	time.sleep(2)

def header_check(spam, header):
	try:
		title = spam.find_element_by_id('workAreaHeader')
		assert title.text == header
		return 'good'
	except:
		return 'bad'

def fail():
	print('Test failed')

def gotoosmanage(driver):
	provs = driver.find_element_by_css_selector('#provisioning_text')
	provs.click()
	time.sleep(.5)
	osimagemange = driver.find_element_by_xpath('//td[2]/a[contains(text(),"Manage OS Images")]')
	osimagemange.click()
	time.sleep(2)
	pas = header_check(driver, 'Deploy Operating Systems: Manage OS Images')
	return pas


def importos(driver,image,condata):
	driver.find_element_by_css_selector('#flexcat_manageOSImage_ManageOSImage_0_importOSBtn').click()
	time.sleep(.5)
	remotetab = driver.find_element_by_xpath('//span[2][contains(text(),"Remote Import")]').click()
	remotetab.send_keys(keys.Keys.TAB, keys.Keys.TAB, keys.Keys.TAB, image)
	#driver.find_element_by_css_selector('#idx_form_TextBox_2').send_keys(image)
	driver.find_element_by_xpath('//div[contains(text(),"Server Name")]').send_keys(keys.Keys.TAB).click()
	#driver.find_element_by_css_selector('.dijitRadio').click()
	driver.find_element_by_id('flexcat_manageOSImage_ImportFile_1_importButton_labelflexcat_manageOSImage_ImportFile_1_importButton_label').click()
	time.sleep(5)
	jobid = getjobid(condata)
	getjobstatus(condata, jobid)
	time.sleep(5)
		





