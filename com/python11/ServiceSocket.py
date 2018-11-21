# -*- coding: UTF-8 -*-

#客户端代码
print("socket实例客户端代码=====================")
import socket
#创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#获取本地主机名, 设置端口
host = socket.gethostname()
port = 8888
#连接服务,指定主机和端口
s.connect((host, port))
#接收小于 1024 字节的数据
msg = s.recv(1024)
print(msg.decode('utf-8'))
s.close()