#! /usr/bin/python3
import paramiko
import sys
import time
#getting connection data 1 is IP, 2 is user, 3 is password.
condata = sys.argv[1],sys.argv[2],sys.argv[3]
#condata = ['10.243.0.23', 'USERID', 'CME44len']

def sshcon(con):
    ssh1 = paramiko.SSHClient()
    ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh1.connect(con[0],username=con[1], password=con[2])
    return ssh1

def get_blades(ssh):
    stdin, stdout, stderr = ssh.exec_command('list -l 2')
    inv1 = stdout.readlines()
    blades1 = []
    for i in inv1:
        if i.startswith('\tblade'):
            blades1.append(i)
    return blades1

def get_switches(ssh):
    stdin, stdout, stderr = ssh.exec_command('list -l 2')
    inv1 = stdout.readlines()
    switches1 = []
    for i in inv1:
        if i.startswith('\tswitch'):
            switches1.append(i)
    return switches1

def get_id(nodes):
    bladeid1 = []
    for server2 in nodes:
        if server2.index(']') == 8:
            bladeid1.append(server2[7:8])
        else:
            bladeid1.append(server2[7:9])
    return bladeid1

def get_switchid(nodes):
    bladeid1 = []
    for server2 in nodes:
        bladeid1.append(server2[8])
    return bladeid1      

def reseat(ssh, bladeids,switchids):
    for blade in bladeids:
        print('Virtually reseating blade['+blade+'] now.')
        ssh.exec_command('service -T blade['+blade+'] -vr')
        time.sleep(5)

    for switch in switchids:
        print('Virtually reseating switch['+switch+'] now.')
        ssh.exec_command('service -T blade['+switch+'] -vr')
        time.sleep(600)
    time.sleep()



ssh = sshcon(condata)

blades = get_blades(ssh)
switches = get_switches(ssh)

bladeid = get_id(blades)
switchid = get_switchid(switches)

print(bladeid)
print(switchid)
try:
    
    while True:
        reseat(ssh,bladeid,switchid)
except:
    print("\nScript Halted!\nClosing ssh session now.")
    ssh.close()
