#!/usr/bin/python
#JJNewbury
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


port = 13000
buf = 1024
host = ("")
addr = (host, port)
global UDPSock
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)

user = str("Users_Online.txt")
users = open(user,"w")
users.close()

def send(kata,userip):
	print (userip)
	pol = 13000
	ipreply = (userip, pol)
	UDPSock.sendto(kata,ipreply)
def receive( threadname,delay):
	while True:
		(data, addr) = UDPSock.recvfrom(buf)
		print (data)
		if data[0][0] == "+":
			users = open(user,"a")
			users.write("\n"+data)
			users.close()
			text = os.linesep.join([l for l in open(user,"r").read().splitlines() if l])
                        users = open(user,'w')
                        users.write(text)
                        users.close()
			print data
		elif data[0][0] == "-":
			data = data.replace("-", "+")
			fin = open(user,'r')
			filedata = fin.read()
			fin.close()
			newdata = filedata.replace(data,"")
			fin = open(user,'w')
			fin.write(newdata)
			fin.close()
			text = os.linesep.join([l for l in open(user,"r").read().splitlines() if l])
			users = open(user,'w')
			users.write(text)
			users.close()
			print (text)
		elif ":GETUSERS" in data:
			#PROBLEM
			a,b = data.split(":")
			a = str(a)
			myfile = open(user,"r")
			kata=myfile.read()
			kata = str(kata)
			myfile.close()
			send(kata, a)
			print (data)
		elif ":connect_to:" in data:
                        a,b,c = data.split(":")
                        a = str(a)
                        #Segment to find user's IP address
                        #dmi variable is binary of value if ip is match
                        dmi = 0
                        #linecheck variable carries while loop through file
                        linecheck = 0
                        userread = open(user,"r")
                        lines=userread.readlines()
                        num = sum(1 for line in open(user))
                        print ("BEFORE WHILE LOOP")
                        while num != linecheck:
                                lol = lines[linecheck]
                                lol =str(lol)
                                x,y = lol.split(":")
                                x = x.replace("+","")
                                x = str(x)
                                a = str(a)
                                if x == a:
                                        linecheck = (num)
                                elif x != a:
                                        linecheck = (linecheck+1)
                        userread.close()
                        userip = (y, port)
			fmi = 0
			linecheck = 0
			userread = open(user,"r")
			lines=userread.readlines()
			num = sum(1 for line in open(user))
			while num != linecheck:
				lol = lines[linecheck]
				lol =str(lol)
				z,v = lol.split(":")
				z = z.replace("+","")
				z = str(z)
				c = str(c)
				if z == c:
					linecheck = (num)
				elif z != c:
					linecheck = (linecheck+1)
			userread.close()
			connectIPaddr = str("IPC-]|[-"+v)
			send(connectIPaddr,y)
		else:
			print(data)

# Create two threads as follows
try:
	thread.start_new_thread( receive, ("Thread-1", 4, ) )
except:
	print "Error: unable to start thread"

while 1:
	pass
