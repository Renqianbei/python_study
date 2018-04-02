#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import _thread
import time


#耗时函数
def printtime(name,delay):
    count = 0
    while count < 5:
        count += 1
        time.sleep(delay)
        print('%s:%s'%(name,time.ctime(time.time())))


#创建线程

try:
    _thread.start_new_thread(printtime,('第一个线程',2))
    _thread.start_new_thread(printtime,('ohter线程',4))
except:
    print('启动线程失败')

while 1:
    pass
