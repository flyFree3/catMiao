#!/bin/python
from socket import socket

def main():
	client = socket()
	client.connect(('192.168.1.78',3333))
	print(client.recv(1024).decode('utf-8'))
	client.close()

main()
