#!/usr/bin/python2
import socket
import time

tcp_server_addr = ('', 5363)

def tcp_recv_server():
    data = 'true'
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.bind(tcp_server_addr)
    tcp_server.listen(128)
    while data:
        time.sleep(1)
        new_tcp, host_info = tcp_server.accept()
        data =time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "---" + str(new_tcp.getpeername())
        print(type(data))
        with open("tcp_source_info.txt","a") as file:
                file.write(str(data))
                file.write('\r\n')
    

tcp_recv_server()
