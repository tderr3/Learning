#! python3



os = {'sles122sap':'/images/SLES/SLES_12_2_SAP.iso','sles123sap':'/images/SLES/SLES_12_3_SAP.iso','rhel69':'/images/RHEL/RHEL-6.9_x64.iso','rhel65':'/images/RHEL/RHEL_6.5_x64.iso','rhel66':'/images/RHEL/RHEL_6.6_x64.iso','rhel68':'/images/RHEL/RHEL-6.8_x64.iso','rhel70':'/images/RHEL/RHEL-7.0_x64.iso','rhel73':'/images/RHEL/RHEL-7.3_x64.iso','rhel74':'/images/RHEL/RHEL-7.4_x64.iso','rhel71':'/images/RHEL/RHEL_7.1_x64.iso','sles114':'/images/SLES/SLES_11_4.iso','sles122':'/images/SLES/SLES_12_2.iso','sles114k':'/images/SLES/SLES_11_4_kiso.iso','sles122k':'/images/SLES/SLES_12_2_kiso.iso','sles114':'/images/SLES/SLES_11_4.iso','sles122':'/images/SLES/SLES_12_2.iso','sles114k':'/images/SLES/SLES_11_4_kiso.iso','sles122k':'/images/SLES/SLES_12_2_kiso.iso','win16':'/images/Windows/Windows_2016_x64.iso','win12':'/images/Windows/Windows_2012_R2_x64.iso','esxi553':'/images/ESXI/ESXi-5-5_u3.iso','esxi51':'/images/ESXI/ESXi5-1_0.iso','esxi513':'/images/ESXI/ESXI5-1_u3.iso','esxi60':'/images/ESXI/ESXI6-0.iso','esxi602':'/images/ESXI/ESXi6-0_u2.iso','esxi603':'/images/ESXI/ESXi6-0_u3.iso','esxi603p':'/images/ESXI/ESXi6-0_u3_purley.iso','esxi65p':'/images/ESXI/ESXi6-5b_purley.iso'}
keys = []
for i in os.keys():
    keys.append(i)

keys.sort()


import sys, pyperclip, time
if len(sys.argv) < 2:
    print('To many Arguments')
    sys.exit()

osimage = sys.argv[1]     # first connand line arg is the account name

if osimage in os:
    pyperclip.copy(os[osimage])
    print('The os image' + osimage+' has been copied to clipboard.')
    sys.exit
else:
    print('There is not os named ' + osimage+'\n')
    for key in keys:
        print(key)
    input()

    
