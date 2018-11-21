# -*- coding: UTF-8 -*-
#网络编程
print("socket实例服务端代码=====================")
#基于socket模块搭建一个简单的server-client系统,服务端启动后一直监听来自客户端的连接并回应"hello world!!!"
#服务端代码

import socket
#创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#获取本地主机名
host = socket.gethostname()
port = 8888
#绑定端口号
s.bind((host,port))
#设置最大连接数,超过后排队
s.listen(5)
while True:
    #建立客户端连接
    client, addr = s.accept()
    print("get connection from %s"%str(addr))
    #回应客户端信息:hello I'am from clinent Python socket!!!
    msg = "hello I'am from clinent Python socket!!!"
    client.send(msg.encode('utf-8'))
    client.close()