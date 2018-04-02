import requests

def restcheck(data):
    check = str(data)
    if check[11:13] == '20':
        return True
    elif check[11:13] == '40':
        return False
    else:
        return 'None'
    
