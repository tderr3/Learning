import time, os, sys, warnings, requests, json, pyperclip

warnings.filterwarnings('ignore')

condata = ['10.243.1.90','USERID','CME44len']

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

jobtrack(condata)
