from selenium import webdriver
import time, os, sys, warnings, requests, json
from selenium.webdriver.common import action_chains, keys
import pyperclip
#from jobtacker import jobtrack


warnings.filterwarnings('ignore')
#print('LXCA IP address?')
#lxcaIp = input()
#lxcaIp = '10.243.1.89'
#lxcaIp = '10.243.13.181'
#lxcaIp = 'https://'+ lxcaIp



def mycon():
	spam1 = webdriver.Firefox(webdriver.FirefoxProfile(os.path.normpath('c:/Automation_web/ffprofile/')))
	spam1.implicitly_wait(20)
	spam1.maximize_window()
	return spam1

def getjobid():
	try:
		test = requests.get('https://10.243.1.89/tasks',auth=('USERID', 'CME44len'), verify=False)
		o = pyperclip.copy(str(test.text))
		test1 = json.loads(str(test.text))
		for i in test1:
			if i['status'] == 'Running': #and [i][0]['category'] == 'OS_DEPLOYMENT':
				job = i['jobUID']
				print(job)
		return job

	except:
		print('null')

def getjobstatus(job):
    job_data = requests.get('https://10.243.1.89/tasks/'+ str(job), verify = False , auth=('USERID' ,'CME44len'))
    job_data = json.loads(str(job_data.text))
    job_status = job_data[0]['status']
    time.sleep(5)
    while job_status == 'Running' or job_status == 'Pending':
        job_data = requests.get('https://10.243.1.89/tasks/'+ str(job), verify = False , auth=('USERID' ,'CME44len'))
        job_data = json.loads(str(job_data.text))
        job_status = job_data[0]['status']

        print('Job at '+str(job_data[0]['percentage'])+'%')
        time.sleep(5)
    #print(job_status)
    return job_data

def setupimageserver(driver):
	count = 0
	servinfo = ['','Image_server', '10.243.1.98', '80', 'FTP', 'CME44len']
	driver.find_element_by_id('provisioning').click()
	time.sleep(.5)
	driver.find_element_by_link_text('Manage OS Images').click()
	time.sleep(2)
	#click config server button
	#click create
	servinfo = ['','Image_server', '10.243.1.98', '80', 'FTP', 'CME44len']
	textbox = driver.find_elements_by_xpath('//input')
	for i in textbox:
		try:
			i.clear()
			i.send_keys(servinfo[cou])

			count = count + 1
		except:

			continue
	#save server button click
	createbut = driver.find_elements_by_xpath('//span[3][contains(@id,"saveServerBtn_label")]')
	clickeybutton(driver, createbut)
			
def clickeybutton(driver, elements):
	for ele in elements:
		try:
			ele.click()
			break
		except:
			continue

			
def login(spam, condata):
        spam.find_element_by_id('idx_form_TextBox_0').send_keys(condata[1])
        spam.find_element_by_id('augusta-login-framePassword').send_keys(condata[2])
        spam.find_element_by_xpath('//span[1]/span/span/span[3][contains(text(),"Log In")]').click()
        time.sleep(2)

def importos(driver, image, condata): #file
	test='Import os'
	prov = driver.find_element_by_id('provisioning')
	prov.click()
	time.sleep(2)
	manos = driver.find_element_by_link_text('Manage OS Images')
	manos.click()
	time.sleep(2)
	driver.refresh()
	time.sleep(5)
	impOS = driver.find_element_by_css_selector('span.dijit:nth-child(4) > span:nth-child(1)')
	impOS.click()
	time.sleep(2)
	remotetab = driver.find_element_by_xpath('//div[3]/div/div/div/div[1]/div[4]/div/div[2]')
	remotetab.click()
	print('click remote tab')
	time.sleep(2)
	imageLoc = driver.find_element_by_xpath('//div/input[contains(@placeholder,"example: /isos/VMWare/6.0u1/LNV2016.iso")][contains(@aria-required, "true")][not(contains(@aria-invalid,"true"))][not(contains(@aria-invalid,"false"))]')
	imageLoc.send_keys(image)
	print('fill in image')
	time.sleep(2)
	#driver.find_element_by_xpath('//tr/td/span[contains(@aria-checked,"false")]').click()
	print('click server button')
	imageLoc.send_keys(keys.Keys.TAB, keys.Keys.TAB, keys.Keys.TAB,keys.Keys.TAB, keys.Keys.TAB, keys.Keys.SPACE)
	time.sleep(1)
	driver.find_element_by_xpath('//span[2]/span[1]/span/span[contains(@id,"importButton")]').click()
	
	'''print('starting count down')
	
	time.sleep(900)
	print('60 min left')
	time.sleep(900)
	print('45 min left')
	time.sleep(900)
	print('30 min left')
	time.sleep(900)
	print('15 min left')
	time.sleep(900)
	print(image+' Done')'''
	time.sleep(5)
	jobtrack(condata)
	time.sleep(3)
	driver.refresh()
	time.sleep(4)
	
	'''jobid = getjobid()
	status = getjobstatus(jobid)
	
	if status['status']['state'] == 'Complete':
		result = 'Passed'
		reportstatus(file,test,result)
	elif status['status']['state'] == 'Failed' or status['status']['state'] == 'Canceled':
		result = 'Failed'
		reportstatus(file,test,result)
		return status
	else:
		return jobid'''

def reportstatus(file,test,result):
	file.write(test+''':          '''+result+'\n')
	
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
	time.sleep(15)
def jobtrack(condata):
    #Gathing job id
    data = requests.get('https://'+condata[0]+'/tasks',auth=(condata[1], condata[2]), verify=False)
    datadic = json.loads(str(data.text))
    try:
        for jobs in datadic:
                print(jobs['status'])
                if jobs['status'] == 'Running':
                        jobid = jobs['jobUID']

    
        print (jobid)
    except NameError:
        print('No running jobs found')

    #tracking Job    
    job_data = requests.get('https://'+condata[0]+'/tasks/'+ str(jobid), verify = False , auth=(condata[1], condata[2]))
    job_data1 = json.loads(str(job_data.text))
    job_status = job_data1[0]['status']
    while job_status == 'Running' or job_status == 'Pending':
        job_data = requests.get('https://'+condata[0]+'/tasks/'+ str(jobid), verify = False , auth=(condata[1], condata[2]))
        job_data1 = json.loads(str(job_data.text))
        job_status = job_data1[0]['status']

        print('Job at '+str(job_data1[0]['percentage'])+'%')
        time.sleep(5)
        #cp = pyperclip.copy(str(job_data.text))
    return job_data1





