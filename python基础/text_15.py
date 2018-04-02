#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys


#os.access(path, mode);

#参数
#path -- 要用来检测是否有访问权限的路径。
#mode -- mode为F_OK，测试存在的路径，或者它可以是包含R_OK, W_OK和X_OK或者R_OK, W_OK和X_OK其中之一或者更多。
#os.F_OK: 作为access()的mode参数，测试path是否存在。
#os.R_OK: 包含在access()的mode参数中 ， 测试path是否可读。
#os.W_OK 包含在access()的mode参数中 ， 测试path是否可写。
#os.X_OK 包含在access()的mode参数中 ，测试path是否可执行。
ret = os.access('text14.txt',os.F_OK)
print(ret)

ret = os.access('/Users/renqianbei/Desktop/python学习/text14.txt',os.R_OK)
print(ret)
ret = os.access('/Users/renqianbei/Desktop/python学习/text14.txt',os.W_OK)
print(ret)
ret = os.access('/Users/renqianbei/Desktop/python学习/text14.txt',os.X_OK)
print(ret)
ret = os.access('/Users/renqianbei/Desktop/python学习/text_15.py',os.X_OK)
print(ret)

#用于改变当前工作目录到指定路径
#os.chdir(path)

reval = os.getcwd()
print('当前工作目录为%s'%reval)
path = '/Users/renqianbei/Desktop'
#修改当前工作目录
os.chdir(path)
reval = os.getcwd()
print('目录修后%s'%reval)


fd = os.open('pythonF1.txt',os.O_RDWR|os.O_CREAT)
os.write(fd,"this is text")



os.closerange(fd,fd)
print ("关闭文件成功!!")

#打开文件
fd = os.open('pythonF2.txt',os.O_RDWR|os.O_CREAT)

#复制文件描述符
d_fd = os.dup(fd)

os.write(d_fd,'this is text'.encode())
os.write(d_fd,'hello温柔的')




os.closerange(fd,d_fd)
print('关闭所有文件成功')



