#! /usr/bin/env python
# -*- coding: utf-8 -*-


class A(object):
    def __init__(self,a,b):
        self.a1 = a
        self.a2 = b
        print('init')
    def mydefault(self,*args):
        print 'defalult:' + str(args[0])
    
    #当调用对象没的方法时  会走这个方法获取默认函数
    def __getattr__(self,name):
        print(name)
        return self.mydefault

a1 = A(10,20)
a1.fn1(1)
a1.fn2('hello')
a1.fn3(2)



def textf (num):
    def xn(va):
        return num * va
    return xn

print(textf(2)(3))
