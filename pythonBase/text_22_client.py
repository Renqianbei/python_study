#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys


clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)

#获取服务端主机名
host = socket.gethostname()
port = 9999

#连接到指定的服务端
clientsocket.connect((host,port))


while True:
    #接受小于1024字节的数据
    print('等待数据到来。。。。')
    msg = clientsocket.recv(1024)
    print('接受到了数据:>>>>>>'+ msg.decode('utf-8'))
    
    msg = input('请输入:')
    clientsocket.send(msg.encode('utf-8'))
    if msg == 'bye':
        print('再见')
        break

print('断开连接')
clientsocket.close()

