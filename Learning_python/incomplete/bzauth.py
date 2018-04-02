import requests
import json
import re
import warnings

warnings.filterwarnings('ignore')
#bz_host = 'bz.labs.lenovo.com'
bz_host = 'bz-test.labs.lenovo.com'

#itcodes =[]
def check_user_lenovo(username):
    print(username)
    #need to talk to steve about getting this info
    '''if username == vendor"
        return 'vendor'
    elif username == lenovo:
        return 'lenovo'
    else:
        return 'not found'''
def get_bug_list_from_Auth_gerneral(bz_host):
    bugs = requests.get('https://'+bz_host+'/rest/bug?bug_status=Open&classification=Tools&product=Bugzilla&component=authorization_general',verify = False)
    bugsdic = json.loads(bugs.text)
    buglist1 = []
    for bugs in bugsdic['bugs']:
        buglist1.append(bugs['id'])
    return buglist1
bugids = get_bug_list_from_Auth_gerneral()

def modbug(bugnumber,bz_host):
    bug = requests.get('https://'+bz_host+'/rest/bug/'+bugnumber, auth=('scripts@lenovo.com', 'Auto1234'), verify=False)
    bugdic = json.loads(bug.text)
    reporterdetail = bugdic['bugs'][0]['creator_detail']
    reporteritcode = reporterdetail['email']
    reporterid = reporterdetail['id']
    userstatus = check_user_lenovo(reporteritcode)

def update_user_lenovo(user,id):
    print(user)
    print(id)
    '''
    add user to lenovo group
    add comment to ticket stating that user is added to lenovo group
    close defect
    '''

def udate_user_vendor(user):
    '''
    add comment to stating that the user is not a lenovo employee and therefore needs to provide more info
    move the ticket to auth vendor
    reject ticket with more info
    '''
def user_already_in_lenovo():
    '''
    add comment 'user' is already in lenovo group please if the intetion was for someone else to be added to the lenovo group please have that user open a ticket to 'component'
    close ticket fixed
    ''' 


#emails = re.findall(r'[\w\.-]+@[\w\.-]+', str(bugsdic))