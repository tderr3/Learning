from lxca_rest_func import *
from LXCA_web_func import *
#from jobgrab import *
from selenium import webdriver
import requests
import json
import sys

#condata = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]]
condata = ['10.243.1.90', 'USERID', 'CME44len', 'UUID']
#os_image = '/images/SLES/SLES_11_4.iso'
#kiso_image = '/images/SLES/SLES_11_4_kiso.iso'
os_image1 = '/images/ESXI/ESXi6-0_u2.iso'
os_image2 = '/images/ESXI/ESXi6-5b_purley.iso'
#os_image =


#setup
#create log
file = open('Kiso_test1.txt', 'w')
file.write('Kiso Test 1\n\n')

#setglobal(condata)
#setupremoteserver(condata)
driver = mycon()
driver.get('https://'+condata[0])

#test
login(driver, condata)

test1 = gotoosmanage(driver)
file. write('Go to  manage os images.\n\n'+test1)


importos(driver, os_image1, condata)
importos(driver, os_image2, condata)











