#! /usr/bin/env python
# -*- coding: utf-8 -*-


#类的专有方法：
#__init__ : 构造函数，在生成对象时调用
#__del__ : 析构函数，释放对象时使用
#__repr__ : 打印，转换
#__str__
#__setitem__ : 按照索引赋值
#__getitem__: 按照索引获取值
#__len__: 获得长度
#__cmp__: 比较运算
#__call__: 函数调用
#__add__: 加运算
#__sub__: 减运算
#__mul__: 乘运算
#__div__: 除运算
#__mod__: 求余运算
#__pow__: 乘方


#运算符重载
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Vector x,y是（%d,%d）'%(self.x,self.y)
    def  __sub__(self,other):
        return  Vector(self.x - other.x,self.y - other.y)

    def __repr__(self):
        return '重新打印的x,y(%d,%d)'%(self.x,self.y)

    def __del__(self):
        print('释放了%s'%self)



v1 = Vector(5,2)
v2 = Vector(1,2)
v3 = v1 - v2
print(v3)

s = str(v3)
print(s)
s = repr(v3)
print(s)

