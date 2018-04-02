import json
import requests
import warnings
import sys
import datetime
import time
from os_deploy_func import getimagelist, deployosstatic, getjobstatus, setglobal

#global condata
datalist = ['LXCA ip: ', 'Username: ', 'Password: ', 'Targert UUID: ', 'OS Static ip: ']
#condata = [sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5]]
condata = ['10.243.2.248','USERID','Passw0rd!','A14365D2FE6C11E69EC4D94D51373DC9', '10.243.1.109']
  
#uuidlist = ['A14365D2FE6C11E69EC4D94D51373DC9', '48C52C45027211E7B65A14365D2FE6C11E69EC4D94D51373DC9DD7C48845B113','214F5B00C3B111E0BEE15CF3FC6E2860']

print('\n')
print('Here is your connection info')
print('\n')
for g,p in zip(datalist, condata):
    print(g + p)
print('\n')

#input data    LXCA IP      USER    Password    Node UUID                       Static IP for os



warnings.filterwarnings('ignore')

#getimage list and set image
print('Gathering image list from LXCA')
imagelist = getimagelist(condata)
print('Here are the images that will be deployed')
for i in imagelist:
    print(i)



#setting default passwords
#print('Setting default os passwords')

#setglobal(condata)

#deploy image
statusfile = open('//home//todd//Documents//Scripts//Status.txt','w')   
for image in imagelist:
    print('Deploying ' + image + ' Now!')
    job = deployosstatic(image, condata)
    status = getjobstatus(job, condata)
    #statusfile = open('c:\\pydata\\status.txt','w')
    if status['status']['state'] == 'Complete':
        print('image ' + image +' deployed successfully!')
        statusfile.write('---------------------------------------------------------\n\n')
        statusfile.write('image ' + image +' deployed successfully!\n\n')
        statusfile.write('---------------------------------------------------------')
        time.sleep(500)
    elif status['status']['state'] == 'Cancelled':
        print('image ' + image +' Cancelled')
        statusfile.write('---------------------------------------------------------\n\n')

        statusfile.write('image ' + image +' cancelled at '+ str(datetime.datetime.now())+'\n\n')
        statusfile.write('status= ' + status['status']['state']+'\n\n')
        for each in status['status']['description']:
            statusfile.write(each['messageDisplay']+'\n\n')
        statusfile.write('---------------------------------------------------------')
        time.sleep(500)

    else:
        print('image ' + image +' failed!')
        statusfile.write('---------------------------------------------------------\n\n')
        statusfile.write('image ' + image +' failed at '+ str(datetime.datetime.now())+'\n\n')
        statusfile.write('status= ' + status['status']['state']+'\n\n')
        #statusfile.write(each['messageDisplay']+'\n\n')
        statusfile.write('---------------------------------------------------------')
        time.sleep(500)
print('All images attempted', '\n', 'Please check c:\pydata\status.txt for results')
statusfile.close()
    



