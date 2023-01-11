import socket
import time

udp_client_address=('192.168.1.71', 3536)

def udp_client_socket():
    udp_socket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
    send_data = "udp data"
    udp_socket.sendto(send_data.encode() , udp_client_address )
    time.sleep(3)
    udp_socket.close()
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
udp_client_socket()