#!/usr/bin/python
import socket
def remotehostinfo():
	rhost = raw_input("Enter Domain:")
	rip = socket.gethostbyname(rhost)
	try:
		print "IP: ", rip
	except socket.error, err_msg:
		print "ERROR"
remotehostinfo()
