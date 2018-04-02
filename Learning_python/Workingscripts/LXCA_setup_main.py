#! python3

from selenium import webdriver
import time
import os
import sys
from selenium.webdriver.common import action_chains, keys
from LXCA_setup_func import mycon, lice, createuser, netconfig, ntp, services, security, finish, partic, callhome, what, warranty
from globalsetup import setglobal, setupremoteserver
#lxcaIp = sys.argv[1]
condata = [sys.argv[1],sys.argv[2]]
#condata = ['10.243.15.73', 'CME44len']

spam = mycon()
spam.implicitly_wait(20)

spam.get('https://'+ condata[0])
time.sleep(5)

spam.maximize_window()
lice(spam)
createuser(spam, condata)
netconfig(spam)
ntp(spam)

try:
    services(spam)
except:
    time.sleep(1)

security(spam)

#setglobalpw(spam)

finish(spam)
'''
print('Changeing Flexcat Global settings now!\n Default OS password same as LXCA')
setglobal(condata)
print('Setting up Remote Image server for OS deploy')
setupremoteserver(condata)
'''
