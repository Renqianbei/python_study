#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

def fuckyou(x):
      print(x*3)
#每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
if __name__ == '__main__':
    print(sys.path)
    print('程序自身在执行')
else:
    print('我来自另一模块')


def sayHello():
    print('helloword')

#内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:

def fbnq(n):
    if n <= 2:
        return 1
    else:
        return fbnq(n-1) + fbnq(n-2)


def fib(n):
    a , b = 0 , 1
    while b < n:
        print(b)
        a,b = b,a+b
    print()


for x in range(1,11):
    print(repr(x), repr(x*x),repr(x*x*x))



#打开一个文件
f = open('mytext.txt','a')
num = f.write("helloword")

#str = f.read()
#str = f.readline()
#str = f.readlines()
#for line in f:
#    print(line)
print(num)


#关闭文件
f.close()




