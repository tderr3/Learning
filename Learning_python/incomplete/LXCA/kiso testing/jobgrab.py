import time
import requests
import json
import warnings
import pyperclip

warnings.filterwarnings('ignore')

#test = requests.get('https://10.243.1.90/jobs',auth=('USERID', 'CME44len'), verify=False)
#condata = ['10.243.1.90', 'USERID', 'CME44len', 'UUID']
#print(test)

#test1 = json.loads(str(test.text))

def getjobid(condata):
	test = requests.get('https://'+condata[0]+'/tasks',auth=(condata[1], condata[2]), verify=False)
	test1 = json.loads(str(test.text))
	for i in test1:
		if [i][0]['status'] == 'Running' or [i][0]['status'] == 'Pending':
			job = [i][0]['jobUID']
			print(job)
			return job



def getjobstatus(condata, job):
    #print('jobstatus')
	#print(condata)
	job_status = requests.get('https://'+condata[0]+'/tasks/'+ str(job), verify = False , auth=(condata[1] ,condata[2]))
	job_status1 = json.loads(job_status.text)
	time.sleep(5)
	while job_status1[0]['status'] == 'Pending':
		job_status = requests.get('https://'+condata[0]+'/tasks/'+str(job), verify = False , auth=(condata[1] ,condata[2]))
		job_status1 = json.loads(job_status.text)
		status1 = str(job_status1[0]['percentage'])
		#print(job_status1)
		try:
			i = len(job_status1[0]['status']['description'])- 1
			message1 = job_status1[0]['status']['description'][i]['messageID']
		except:
			message1 = 'No Message'
		jobstatus2 = 'Job is ' +status1+ '% complete: ' + message1 
		print(jobstatus2)
		#return jobstatus2
		time.sleep(3)
	return job_status1
#jobid = getjobid(condata)
#state = getjobstatus(condata, jobid)



