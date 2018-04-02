#! /usr/bin/env python
# -*- coding: utf-8 -*-

#类
class Person:
    name = ''
    age = 0
    #类的方法  第一个参数 代表当前类的实例 取名随意 一般取名self
    #    很多类都倾向于将对象创建为有初始状态的。因此类可能会定义一个名为 __init__() 的特殊方法（构造方法）
    #类定义了 __init__() 方法的话，类的实例化操作会自动调用 __init__() 方法
    def __init__(self,n,a):
        self.name = n
        self.age = a
    #类的方法  第一个参数 代表当前类的实例 取名随意 一般取名self
    def prt(m):
        print(m.name+repr(m.age)+'岁')
        print(m.__class__)

    def  say(self,word):
        print(self.name + '说了' + str(word))

p = Person('Predor',100)
p.prt()
p.say('妈卖批')
print(p.name)

class Woman:
    def __init__(self,cup):
        self.cup = cup

#继承
class Student(Person):
    chengji = 0
    father = None
    mother = None
    def __init__(self,n,a,f = None,m = None):
        #调用父类的构造函数
        Person.__init__(self,n,a)
        self.father = f
        self.mother = m
    def say(self,word):
        print('%s今年%s岁  爸爸是: %s 妈妈是%s'%(self.name,self.age,self.father,self.mother) + '\n'+word)



s = Student('牛顿',2,p)
s.say('妈卖批')
s.prt()

#多重继承
class KongJie(Person,Woman):
    elepany = '波音747'
    # __ 私有变量
    __siyoubianliang = '1000'
    def __init__(self,n,a,cup,f=None,m=None):
        Person.__init__(self,n,a)
        Woman.__init__(self,cup)

    def say(self):
        print('======\n'+self.name+str(self.age) + '岁 '+self.cup+' elepany:'+self.elepany)
        print(self.__siyoubianliang)
    # __ 私有方法
    def __siyouMethod(self):
        print(self.name,self.__siyoubianliang)

one = KongJie('丫丫',20,'34B',p)
one.say()
print(one.name)
#私有变量外部不能访问
#print(one.__siyoubianliang)

