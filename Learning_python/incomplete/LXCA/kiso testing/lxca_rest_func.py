import json
import requests
import time
import sys
import warnings
import subprocess

warnings.filterwarnings('ignore')


def setglobal(condata):
	print('Updateing global settings now.', '\n')
	print(condata[1] +' '+ condata[0])
	payload1 = {'credentials': [{'type': 'LINUX', 'password': 'CME44len', 'passwordChanged': True}, {'type': 'ESXi', 'password': 'CME44len', 'passwordChanged': True}, {'type': 'RHEL/ESXi', 'password': 'CME44len', 'passwordChanged': True}, {'type': 'WINDOWS', 'password': 'CME44len', 'passwordChanged': True}]}
	gbset1 = requests.put('https://'+condata[0]+'/osdeployment/globalSettings',auth=('USERID',condata[1]), verify= False, json=payload1, timeout=60.0)
	gbset2 = json.loads(str(gbset1.text))
	if str(gbset1) == '<Response [200]>':
		print('Global settings changed succesfully','\n')
	else:
		print(gbset2['messages'][0]['text'] + ' Becuase '+ b['messages'][0]['explanation'])

def setupremoteserver(condata):
	print('Setting up remote image server now.')
	payload = {"address":"10.243.1.98","displayName":"test","password":"CME44len","port":80,"protocol":"HTTP","username":"FTP"}
	remoteserver = requests.post('https://'+condata[0]+'/osImages/remoteFileServers', auth=('USERID',condata[1]), verify=False, json=payload)
	remoteserver1 = json.loads(str(remoteserver.text))
	if str(remoteserver) == '<Response [200]>':
		print('Remote OS image server has been configured.','\n')
	else:
		print(remoteserver1['messages'][0]['text'] + ' Becuase '+ b['messages'][0]['explanation'], '\n')
def test():
	print('worked')
