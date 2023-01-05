#!/bin/python
from socket import socket,AF_INET,SOCK_STREAM
from datetime import datetime
# windows execute telnet 192.168.1.78 3333

def main():
	#创建ipv4，tcp套接字
	server = socket(family = AF_INET,type=SOCK_STREAM)
	#绑定服务器ip及端口
	server.bind(('192.168.1.78',3333))
	#监听连接到服务的客户端
	server.listen(10)
	print('Start to listen ……')

	while True:
		client , addr = server.accept()
		print(str(addr) + 'connect to server')
		client.send(str(datetime.now()))
		client.close()

main()



