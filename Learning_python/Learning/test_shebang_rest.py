#! python3

import requests
import sys
import json

ip = sys.argv[1]

print(ip)

test = requests.get('https://'+ip+'hostPlatforms/', auth=('USERID','CME44len'),verify=False)

testdata = json.loads(str(test.text))

file = open('c:\\pydata\\osoutput.txt','w')

file.write(testdata)

file.close()

