#!/usr/bin/python
#JJNewbury
import sys
import socket as so
import platform
from socket import *
import string
import base64
import os
from os.path import expanduser
import random
import thread
import time
from urllib2 import urlopen
from sys import platform as _platform
from json import load
homeuser = expanduser("~")
filename = str(homeuser+"/Documents/Ogle/Users.txt")
# Color Class
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

# Load's Files
if os.path.exists(homeuser+"/Documents/Ogle/") == True:	
	if os.path.isfile(homeuser+"/Documents/Ogle/Users.txt") == True:
		s = str(bcolors.OKBLUE + "User List Loaded: " + bcolors.ENDC)
		for c in s:
			sys.stdout.write( '%s' % c )
			sys.stdout.flush()
			time.sleep(0.05)
	elif os.path.isfile(homeuser+"/Documents/Ogle/Users.txt") == False:
		users = file(homeuser+"/Documents/Ogle/Users.txt","w")
		s = str(bcolors.OKBLUE + "Creating User List: " + bcolors.ENDC)
		for c in s:
			sys.stdout.write( '%s' % c )
			sys.stdout.flush()
			time.sleep(0.05)
elif os.path.exists(homeuser+"/Documents/Ogle/") == False:	
		os.makedirs(homeuser+"/Documents/Ogle/")
		users = file(homeuser+"/Documents/Ogle/Users.txt","w")
		s = str(bcolors.OKBLUE + "Creating User List: " + bcolors.ENDC)
		for c in s:
			sys.stdout.write( '%s' % c )
			sys.stdout.flush()
			time.sleep(0.05)
		s = str(bcolors.OKBLUE + "Creating User List: " + bcolors.ENDC)
		for c in s:
			sys.stdout.write( '%s' % c )
			sys.stdout.flush()
			time.sleep(0.05)

s = str(bcolors.OKBLUE + "Boot loading initialized" + bcolors.ENDC)
for c in s:
	sys.stdout.write( '%s' % c )
	sys.stdout.flush()
	time.sleep(0.05)
# Starts networking
exip = load(urlopen('http://jsonip.com'))['ip']
host = ("")
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)

# Starts Main Menu
i = 0
while i == 0:
	if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
		os.system("clear")
	elif _platform == "win32":
		os.system('cls')
	print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
	print ("|			Welcome! Choose from one of the following:         |")		
	print ("|		 1) Manage Contacts                                    |")
	print ("|		 2) Initiate Messenger                                 |")	
	print ("        Your IP Address: "+exip)			
	print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
	choice = input("\n> Enter the corresponding number to your choice: ")
	if choice == 1:
		if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
			os.system("clear")
		elif _platform == "win32":
			os.system('cls')
		print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		print ("|               		   Options:                               |")
		print ("|        1) View Contacts                                         |")
		print ("|        2) Add Contacts                                          |")
		print ("|        3) Remove Contacts                                       |")
		print ("|        4) Back to Main Menu                                     |")
		print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		choice = input("\n> Enter the corresponding number to your choice: ")
		if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
			os.system("clear")
		elif _platform == "win32":
			os.system('cls')
		if choice == 1:
			user = str(homeuser+"/Documents/Ogle/Users.txt")
			userread = open(user,"r")
			linecheck = 0
			lines=userread.readlines()
			num = sum(1 for line in open(user))
			print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
			key = str(bcolors.UNDERLINE + "Name::IP Address" + bcolors.ENDC)
			print ("        "+key)
			print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
			while num != linecheck:
				lol = lines[linecheck]
				lol =str(lol)
				print ("      "+lol)
				linecheck = (linecheck+1)
			choice = input("\n> Type '1' to return to Main Menu: ")
			if choice == 1:
				if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
					os.system("clear")
				elif _platform == "win32":
					os.system('cls')
			else:
				print ("> Does not comply...")
				time.sleep(2.5)
				print ("> Exiting to Main Menu...")
				if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
					os.system("clear")
				elif _platform == "win32":
					os.system('cls')
			userread.close()
		elif choice == 2:
			if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
				os.system("clear")
			elif _platform == "win32":
				os.system('cls')
			tick = 0
			while tick == 0:
				print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
				print ("|     1) Add New Contact                |")
				print ("|     2) Back to Main Menu              |")
				print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
				inpurt = input("\n> Enter the corresponding number to your choice: ")
				if inpurt == 1:
					name = raw_input("\n> Enter name of user: ")
					ip_address = raw_input("> Enter IP address of user: ")
					additon = str(name+"::"+ip_address)
					file = open(filename,"a")
					file.write("\n"+additon)
					file.close()
				elif inpurt == 2:
					tick = (tick + 1)
		elif choice == 3:
			if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
				os.system("clear")
			elif _platform == "win32":
				os.system('cls')
			user = str(homeuser+"/Documents/Ogle/Users.txt")
			userread = open(user,"r")
			linecheck = 0
			lines=userread.readlines()
			num = sum(1 for line in open(user))
			print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
			key = str(bcolors.UNDERLINE + "Name::IP Address" + bcolors.ENDC)
			print ("        "+key)
			print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
			while num != linecheck:
				mun = str(linecheck+1)
				lol = lines[linecheck]
				lol =str(mun+") "+lol)
				print ("      "+lol)
				linecheck = (linecheck+1)
			print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
			userread.close()
			userremove = input("\n> Enter corresponding number to your choice of user to be removed: ")
			user = str(homeuser+"/Documents/Ogle/Users.txt")
			userread = open(user,"r")
			linecheck = 0
			lines=userread.readlines()
			num = sum(1 for line in open(user))
			while num != linecheck:
				mun = str(linecheck+1)
				lol = lines[linecheck]
				lol =str(mun+") "+lol)
				lineremove = str("      "+lol)
				if mun == userremove:
					userread.close()
					f = open(user,'r')
					filedata = f.read()
					f.close()
					newdata = filedata.replace(lineremove,"")
					f = open(user,'w')
					f.write(newdata)
					f.close()
					text = os.linesep.join([l for l in open(user,"r").read().splitlines() if l])
					users = open(user,'w')
					users.write(text)
					users.close()
					linecheck = (num)
				elif mun != userremove:
					linecheck = (linecheck + 1)
		elif choice == 4:
			print ("")
	elif choice == 2:
		if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
			os.system("clear")
		elif _platform == "win32":
			os.system('cls')
		user = str(homeuser+"/Documents/Ogle/Users.txt")
		userread = open(user,"r")
		linecheck = 0
		lines=userread.readlines()
		num = sum(1 for line in open(user))
		print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		key = str(bcolors.UNDERLINE + "Name::IP Address" + bcolors.ENDC)
		print ("        "+key)
		print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		while num != linecheck:
			mun = str(linecheck+1)
			lol = lines[linecheck]
			lol =str(mun+") "+lol)
			print ("      "+lol)
			linecheck = (linecheck+1)
		print ("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		userread.close()
		userchat = input("\n> Enter corresponding number to your choice of user to chat with: ")
		user = str(homeuser+"/Documents/Ogle/Users.txt")
		userread = open(user,"r")
		linecheck = 0
		lines=userread.readlines()
		num = sum(1 for line in open(user))
		while num != linecheck:
			mun = str(linecheck+1)
			lol = lines[linecheck]
			lob =str(mun+") "+lol)
			lineremove = str("      "+lol)
			if mun == userchat:
				a,b = lol.split("::")
				global chatip
				chatip = str(b)
				global chatnet
				chatnet = (b,port)
				linecheck = (num)
				i = (i+1)
			elif mun != userchat:
				linecheck = (linecheck + 1)
				
name = raw_input("\n> Enter your username: ")
s = str(bcolors.OKBLUE + "Initiating Ogle Messenger...Press Ctrl+C to exit script..." + bcolors.ENDC)
for c in s:
	sys.stdout.write( '%s' % c )
	sys.stdout.flush()
	time.sleep(0.05)

# Functions
def send( threadname,delay):
	while True:
		datal = raw_input("")
		datal = (name+": "+datal)
		UDPSock.sendto(datal, chatnet)
		
def receive( threadname,delay):
	while True:
		(data, addr) = UDPSock.recvfrom(buf)
		print (data)
		
# Threads
try:
	thread.start_new_thread( send, ("Thread-1", 2, ) )
	thread.start_new_thread( receive, ("Thread-2", 4, ) )
except KeyboardInterrupt:
	print ("Goodbye!")

while 1:
	pass
