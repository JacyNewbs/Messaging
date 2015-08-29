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
from urllib2 import urlopen
from json import load

name = str("bladder1")
host = ("")
BLOCK_SIZE = 32
hostl = str("bladder2")
port = 13000
buf = 1024
addr = (host, port)
addrl = (hostl, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
# Define a function for the thread
def send( threadname,delay):
	while True:
		datal = raw_input("")
		datal = (name+": "+datal)
		UDPSock.sendto(datal, addrl)
		
def receive( threadname,delay):
	while True:
		(data, addr) = UDPSock.recvfrom(buf)
		print (data)

# Create two threads as follows
try:
	thread.start_new_thread( send, ("Thread-1", 2, ) )
	thread.start_new_thread( receive, ("Thread-2", 4, ) )
except KeyboardInterrupt:
	print ("Goodbye!")

while 1:
	pass
