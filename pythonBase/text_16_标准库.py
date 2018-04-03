#! /usr/bin/env python
# -*- coding: utf-8 -*-


#操作系统接口
#os模块提供了不少与操作系统相关联的函数。

#os
import os
os.getcwd()
os.chdir('/Users/renqianbei/Desktop')
os.system('touch  data.db')

#dir(os)
#help(os)

#针对日常的文件和目录管理任务，:mod:shutil 模块提供了一个易于使用的高级接口:
import shutil
shutil.copyfile('data.db','data1.db')
shutil.move('data1.db','/Users/renqianbei/Desktop/hello.db')

#文件通配符
#glob模块提供了一个函数用于从目录通配符搜索中生成文件列表:

os.chdir('/Users/renqianbei/Desktop')
import glob
l = glob.glob('Saas*')
print(l)

#命令行参数
#通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于 sys 模块的 argv 变量。例如在命令行中执行 "python3 text_16_标准库.py hello word " 后可以得到以下输出结果:
#['text_16_标准库.py', 'hello', 'word']
import sys
print(sys.argv)

#字符串正则匹配
#re模块为高级字符串处理提供了正则表达式工具。对于复杂的匹配和处理，正则表达式提供了简洁、优化的解决方案:
import re
#使用正则表达式
s = re.findall(r'\bf[a-z]*','which foot or hand fell fastest')
print(s)
#['foot', 'fell', 'fastest']

#字符串替换
s = 'tea for too'.replace('too','two')
print(s)

#数学
import math
print(math.sin(math.pi/2))
print(math.log(1024,2))

#随机
import random
s = random.choice(['1','red','phone'])
print(s)
# sampling without replacement 不重复随机
s = random.sample(range(100),10)
print(s)
 # random float
print(random.random())
# random integer chosen from range(6)
print(random.randrange(6))




#日期
from datetime import date
now = date.today()
print(now)
s = now.strftime('%m-%d-%y. %d %b %Y is a %A on the %d day of %B.')
print(s)
s = now.strftime('%Y-%m-%d')
print(s)

birthday = date(1990,8,14)
age = now - birthday
print(age.days)


#性能度量
#有些用户对了解解决同一问题的不同方法之间的性能差异很感兴趣。Python 提供了一个度量工具，为这些问题提供了直接答案。
#例如，使用元组封装和拆封来交换元素看起来要比使用传统的方法要诱人的多,timeit 证明了现代的方法更快一些。
from timeit import Timer
s = Timer('t=a;a=b;b=t','a=1;b=2').timeit()
print(s)
s = Timer('a,b = b,a','a=1;b=2').timeit()
print(s)

#访问互联网
#几个模块用于访问互联网以及处理网络通信协议。其中最简单的两个是用于处理从 urls 接收的数据的 urllib.request 以及用于发送电子邮件的 smtplib:


import urllib
from urllib.request import urlopen
from urllib.parse import urlencode

loginUrl = 'http://devi.haokeduo.com/appc/public/Login'
para = {'tel':'18611404533','pw':'w123456'}

req_data = urlencode(para) #将字典类型的请求数据转变为url编码
#tel=18611404533&pw=w123456
print(req_data)

#处理get请求，不传data，则为get请求
url = loginUrl + '?' + req_data
print(url)
#通过urlopen方法访问拼接好的url
res = urlopen(url)

res = res.read().decode()#read()方法是读取返回数据内容，decode是转换返回数据的bytes格式为str
print(res)

from urllib.request import Request
#处理post请求,如果传了data，则为post请求
data=req_data.encode('ascii') #将url编码类型的请求数据转变为bytes类型
request = Request(loginUrl,req_data)#将url和请求数据处理为一个Request对象，供urlopen调用
with  urlopen(request) as res:
       res = res.read().decode()#read()方法是读取返回数据内容，decode是转换返回数据的bytes格式

print(res)

