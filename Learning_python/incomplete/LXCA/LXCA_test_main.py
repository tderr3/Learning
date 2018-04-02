#! python3
from LXCA_web_func import *


condata = ['10.243.1.89','USERID','CME44len']
image = '/images/SLES/SLES_12_2.iso'

driver = mycon()

driver.get('https://'+condata[0])
time.sleep(2)

login(driver,condata)

#setglobalpw(driver)


file = open('C://Python34//Scripts//incomplete//LXCA//test_logs//logfile.txt','w')
file.write(''.center(60, '*'))
file.write('\n')
file.write(' LXCA WEB UI TESTING '.center(60, '*'))
file.write('\n')
file.write(''.center(60, '*'))
file.write('''



''')

i = importos(driver, image, file)


file.close()


