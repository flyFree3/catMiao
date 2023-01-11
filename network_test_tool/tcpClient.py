import socket
tcp_client_address=('192.168.1.71', 5363)


#创建服客户端TCP_socket
def tcp_send_client():
    """使用tcp发送数据"""
    # 创建tcp套接字
    tcp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    # 连接服务器
    tcp_socket.connect(tcp_client_address)
    # 发送数据
    data = 'data'
    tcp_socket.send(data.encode())
    # 断开连接
    tcp_socket.close()

tcp_send_client()
