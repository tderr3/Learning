import requests
import json
import time
import warnings


warnings.filterwarnings('ignore')
condata = ['10.243.1.90','USERID','CME44len']
payload1 = {'userPw':condata[2],'userName':condata[1],'groups':['lxc-supervisor'],'PasswordChangeFirstAccess':False}


userCreate = requests.post('https://'+condata[0]+'/userAccounts', verify=False, json=payload1)
text = json.loads(str(userCreate.text))
check = str(userCreate)
if check[11:14] == '201':
    print('User created sucsessfully')
else:
    print(text['messages'][0]['recovery']['text'])
    exit
time.sleep(2)
payload2 = {"isServiceAndSupportStep4Configured": True,"isNetworkAccessConfigured": True,"isDemoSkipped": True,"isServiceAndSupportStep1Configured": True,"isLicenseAccepted": True,"isRestoredFromBackup": False,"isUserCreated": True,"isServiceAndSupportStep2Configured": True,"isServiceAndSupportStep3Configured": True,"isDateAndTimeConfigured": True,"isSecurityConfigured": True,"isServiceAndSupportConfigured": True}

skipSetup = requests.put('https://'+condata[0]+'/initialSetup',auth=(condata[1],condata[2]), verify=False, json=payload2)

text = json.loads(str(skipSetup.text))
check = str(userCreate)
if check[11:14] == '200':
    print('User created sucsessfully')
else:
    print(check)
    print(text['messages'][0]['recovery']['text'])
    exit

