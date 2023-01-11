#!/usr/bin/python
import socket
import time

udp_server_addr = ('',3536)

def udp_server_socket():
    data = 'true'
    while data:
        print('aaa')
        udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        udp_socket.bind(udp_server_addr)
        data =time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "---" + str(udp_socket.recvfrom(1024))
        print(type(data))
        with open("udp_source_info.txt","a") as file:
		    file.write(str(data))
		    file.write('\r\n')

udp_server_socket()
