import webdriver as dr
from selenium import webdriver
import requests, time, os, sys
from LXCA_web_func import login, importos

#image_list =['/images/ESXI/ESXi-5-5_u3.iso','/images/ESXI/ESXi6-0_u3.iso','/images/ESXI/ESXi6-5b_purley.iso','/images/ESXI/ESXI6-0.iso']
image_list =['/images/RHEL/RHEL-6.9-20170226.0-Server-x86_64-dvd1.iso','/images/RHEL/RHEL_7.1_x64.iso','/images/SLES/SLES_11_4.iso','/images/SLES/SLES_12_2.iso','/images/Windows/Windows_2016_x64.iso','/images/Windows/Windows_2012_R2_x64.iso']
'''
driver = dr.mycon()

condata = ['10.243.1.100','USERID','CME44len']

driver.get('https://'+condata[0])
time.sleep(1)

driver.maximize_window()
login(driver, condata)
time.sleep(2)

for os in image_list:
    importos(driver, os, condata)
    

'''
