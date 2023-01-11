tcp连接：
1、修改tcpServer.py文件中的tcp_server_addr参数，设置监听端口
2、在终端执行 nohup ./tcpServer.py &
3、修改tcpClient.py文件中的参数tcp_client_address，ip为终端ip，端口与步骤1监听端口一致
4、本地运行tcpClient.py
5、成功的tcp连接，会记录连接时间、源IP及源端口至tcp_source_info.txt

udp连接：
1、修改udpServer.py文件中的udp_server_addr参数，设置监听端口
2、在终端执行 nohup ./udpServer.py &
3、修改udpClient.py文件中的参数udp_client_address，ip为终端ip，端口与步骤1监听端口一致
4、本地运行udpClient.py
5、成功的udp连接，会记录连接时间、源IP及源端口至udp_source_info.txt



