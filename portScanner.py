#!usr/bin/python

import socket 

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.setdefaulttimeout(1)

host = input("Enter host ip")
port = int(input("Enter port "))

def scan(port):
	if sock.connect_ex((host,port)):
		print("port" ,port , "is closed")
	else:
		print("port" ,port , "is opened")


scan(port)
