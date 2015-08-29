#!/usr/bin/python
#JJNewbury

import subprocess
import sys
import socket as so
import platform
from socket import *
import string
import base64
import os
import random
import thread
import time
from urllib2 import urlopen
from json import load
#Get External IP Address
exip = load(urlopen('http://jsonip.com'))['ip']

name = raw_input("Enter your username: ")
dmi = 0
lmi = 0	
host = ("")
checkcode = ''.join(random.choice('0123456789QWERTYUIOPLKJHGFDSAZXCVBNMasdfgjhklpoiuytrewqmnzbxvc') for i in range(16))
BLOCK_SIZE = 32
hostl = str("37.187.19.162")
port = 13000
buf = 1024
addr = (host, port)
addrl = (hostl, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
addr = (host, port)
addrl = (hostl, port)
login = str("+"+name+":"+exip)
userdata = str(exip+":GETUSERS")
UDPSock.sendto(login, addrl)
CONNECTORIP = ""
# Define a function for the thread
def send( threadname,delay):
	while True:
		datal = raw_input("")
		if datal == "Users":
			UDPSock.sendto(userdata,addrl)
		elif datal == "Help":
			print ("Commands:")
			print ("Users : Lists all online users")
			print ("exit() : Exits program")
			print ("connect_to:<username> : Connects you to desired user")
		elif "connect_to:" in datal:
			a,b = datal.split(":")
			pep = str(name+":connect_to:"+b)
			UDPSock.sendto(pep,addrl)
		elif "exit" in datal:
			logout = str("-"+name+":"+exip)
			UDPSock.sendto(logout,addrl)
			print ("Logged out..")
			print ("You can now close, Thank you.")
		else:
			print("prb")
		
def receive( threadname,delay):
	while True:
		(data, addr) = UDPSock.recvfrom(buf)
		if "IPC-]|[-" in data:
			data = str(data)
			a,b = data.split("-]|[-")
			CONNECTORIP = str(b)
			
			f = open("MESSENGER.py",'r')
			filedata = f.read()
			f.close()

			newdata = filedata.replace("bladder1",name)

			f = open("MESSENGER.py",'w')
			f.write(newdata)
			f.close()
			
			f = open("MESSENGER.py",'r')
			filedata = f.read()
			f.close()
			CONNECTORIP = str(CONNECTORIP)
			CONNECTORIP = CONNECTORIP.replace("\n", "")
			newdata = filedata.replace("bladder2",CONNECTORIP)

			f = open("MESSENGER.py",'w')
			f.write(newdata)
			f.close()
			print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
			print ("|  Close this program, then   |")
			print ("|  Run 'MESSENGER.py' to chat |")
			print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
			sys.exit("")
			
		else:
			print (data)

# Create two threads as follows
try:
	thread.start_new_thread( send, ("Thread-1", 2, ) )
	thread.start_new_thread( receive, ("Thread-2", 4, ) )
except KeyboardInterrupt:
	UDPSock.sendto(login, addrl)
	print ("Exiting")

while 1:
	pass
