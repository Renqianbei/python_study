#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
            print("Oops!  That was no valid number.  Try again   ")



try:
    f = open('myfile.txt','w+')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print('OSError:{0}'.format(err))
except ValueError:
    print("无法将数据转换成int")
except IOError:
    print('文件读权限错误')
except :
    print('未知的错误',sys.exc_info()[0])
    raise


class MYError(Exception):
    def __init__(self,value):
            self.name = value
    def __str__(self):
        return repr(self.name)


try:
    raise MYError('oops!')
except MYError as e:
    print('my exception occurred，value = ',e.name)





