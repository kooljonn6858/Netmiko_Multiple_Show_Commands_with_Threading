from netmiko import ConnectHandler
from datetime import datetime
from threading import Thread
from getpass import getpass

starttime = datetime.now()

USER = input('Input Username: ')
PASS = getpass()

threads = []

print("Start time is:", starttime)

def checkparallel(ip):
	net_connect = ConnectHandler(device_type='cisco_ios', ip=DEVICE, username=USER, password=PASS)
	with open('show_commands') as COMMANDS:
		output = ''
		for CMD in COMMANDS:
			output += DEVICE + '\n' + CMD + net_connect.send_command(CMD) + '\n' + '+'*80 + '\n'
		print(output)
	net_connect.disconnect()

with open('device_list') as DEVICE_LIST:
	for DEVICE in DEVICE_LIST:
		t =  Thread(target=checkparallel, args=(DEVICE,))
		t.start()
		threads.append(t)

for t in threads:
    t.join()


total_time = datetime.now() - starttime

print("Total execution time is:", total_time)

