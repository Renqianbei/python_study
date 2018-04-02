#! /usr/bin/env python3
# -*- coding: utf-8 -*-


#socket
#服务端

import socket
import sys

#参数
#socket.socket(family, type, proto)
#family: 套接字家族可以使AF_UNIX或者AF_INET
#type: 套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM
#protocol: 一般不填默认为0.
#创建socket对象
serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)

# 获取本地主机名
host =socket.gethostname()
port = 9999
print(host)
#绑定端口
serversocket.bind((host,port))

#设置最大链接数
serversocket.listen(5)
#建立客户端链接  接受连接  阻塞线程
clientsocket,addr  =  serversocket.accept()

print("建立了连接地址：%s ===="%str(addr))
msg = '欢迎访问我的服务器!'
clientsocket.send(msg.encode('utf-8'))

while True:
    print('等待数据到来。。。。')
    msg = clientsocket.recv(1024)
    print('接受到了数据>>>>:'+msg.decode('utf-8'))
    if msg.decode('utf-8') == 'bye':
        print('再见')
        break
    msg = input('请输入:')
    clientsocket.send(msg.encode('utf-8'))


print('断开连接')
clientsocket.close()
