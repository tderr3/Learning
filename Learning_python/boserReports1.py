import requests
global key, bz
key='AirXEelVqsNtHp4I3OwavnZpVBcG5OdaKf8zuU0S'
bz='https://bz.labs.lenovo.com'

def getBugList():
    fullBugList =[]
    search=requests.get(bz+'/rest/bug?bug_status=Open&bug_status=Working&bug_status=Rejected&classification=Software&product=XClarity%20Administrator&resolution=---&api_key='+key,verify=False)
    for bug in search.json()['bugs']:
        fullBugList.append(bug['id'])
        
    
    return fullBugList


'''

def bugChecker(bugList):
    Loop through history and check if change was to product and check if change was to rejected
    
    loop
    if change is to field product and 1 to count
    

    loop
    if change is to field status and new status is rejected and 1 to count
    after looping through all history for a bug check if it > threshold then add to the list
    
    
    
    return True


    return False
def generateReport():
    
    return None
'''
list1 = getBugList()
print(list1)    
    