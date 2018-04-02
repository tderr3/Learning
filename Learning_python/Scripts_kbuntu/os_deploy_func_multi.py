import json
import requests
import time
import sys
import warnings
import subprocess
#global condata
warnings.filterwarnings('ignore')
'''
def pingtest(condata):
	res1 = subprocess.call(['ping', condata[4])
	return res1'''



def getimagelist(condata):
		#print('getimagelist')
		#print(condata)
		test = requests.get('https://'+ condata[0] +'/hostPlatforms', auth= (condata[1] , condata[2]), verify=False)
		test_dict = json.loads(test.text)
		images = test_dict.get('availableImages')
		imagelist1 = []
		for i in range(len(images)):
			imagelist1.append(images[i])
		return imagelist1
	
	
def deployosstatic(image, condata):
    #print('depolystatic')
    #print(condata)
        if condata[3] == 'A14365D2FE6C11E69EC4D94D51373DC9':
            mac = '08:94:EF:3F:ED:05'
        elif condata[3] == '48C52C45027211E7B65DD7C48845B113':
            mac = '08:94:EF:40:8C:1C'
        elif condata[3] == '214F5B00C3B111E0BEE15CF3FC6E2860':
            mac = '5C:F3:FC:6E:28:60'
        else:
            mac = 'AUTO'
        payload1 = [{"networkSettings":{"gateway":"10.243.0.1","ipAddress":condata[4],"selectedMac":mac,"subnetMask":"255.255.240.0"},"selectedImage":image,"storageSettings":{"targetDevice":"localdisk"},"uuid":condata[3]}]
        deploy1 = requests.put('https://'+ condata[0] + '/hostPlatforms', auth=(condata[1] , condata[2]), verify=False, json=payload1)
        print(deploy1)
        deploy2 = json.loads(str(deploy1.text))
        jobid2 = deploy2.get('jobId')
        print('Deploy kick off was successful. Job id is ' + str(jobid2) , '\n')
        return jobid2

def getjobstatus(job, condata):
	#print('jobstatus')
	#print(condata)
	job_status = requests.get('https://'+condata[0]+'/jobs/'+ str(job), verify = False , auth=(condata[1] , condata[2]))
	job_status1 = json.loads(job_status.text)
	status1 = job_status1.get('status')
	time.sleep(5)
	while status1.get('state') == 'Running' or status1.get('state') == 'Pending':
		job_status = requests.get('https://'+condata[0]+'/jobs/'+ str(job), verify = False , auth=(condata[1] , condata[2]))
		job_status1 = json.loads(job_status.text)
		status1 = job_status1.get('status')
		#print(job_status1)
		'''try:
			i = len(job_status1['status']['description'])- 1
			message1 = job_status1['status']['description'][i]['messageID']
		except:
			message1 = 'none' '''
		jobstatus2 = 'Job is ' + str(status1['percentage'])+ '% complete '# + message1 
		print(jobstatus2)
		#return jobstatus2
		time.sleep(5)
	return job_status1
	
def setglobal(condata):
	print('Updateing global settings now.', '\n')
	payload1 = {'credentials': [{'type': 'LINUX', 'password': 'CME44len', 'passwordChanged': True}, {'type': 'ESXi', 'password': 'CME44len', 'passwordChanged': True}, {'type': 'RHEL/ESXi', 'password': 'CME44len', 'passwordChanged': True}, {'type': 'WINDOWS', 'password': 'CME44len', 'passwordChanged': True}]}
	gbset1 = requests.put('https://'+condata[0]+'/osdeployment/globalSettings',auth=(condata[1],condata[2]), verify= False, json=payload1)
	gbset2 = json.loads(str(gbset1.text))
	#if str(gbset1) == '<Response [200]>':
		#print('Global settings changed succesfully','\n')
	#else:
		#print(gbset2['messages'][0]['text'] + ' Becuase '+ b['messages'][0]['explanation'])

def setupremoteserver(condata):
	print('Setting up remote image server now.')
	payload = {"address":"10.243.1.98","displayName":"test","password":"CME44len","port":80,"protocol":"HTTP","username":"FTP"}
	remoteserver = requests.post('https://'+condata[0]+'/osImages/remoteFileServers', auth=(condata[1],condata[2]), verify=False, json=payload)
	remoteserver1 = json.loads(str(remoteserver.text))
	#if str(remoteserver) == '<Response [200]>':
		#print('Remote OS image server has been configured.','\n')
	#else:
		#print(remoteserver1['messages'][0]['text'] + ' Becuase '+ b['messages'][0]['explanation'], '\n')


