#! /usr/bin/env python
# -*- coding: utf-8 -*-



# 打开文件     r  w  a    r+  w+  a+

f = open('text14.txt','w+')
l = f.write('写入了部分字符串')
print(l)
#f.close()


f = open('text14.txt','a+')
m = f.write('\n 追加部分内容')
print(m)
#f.close()

f = open('text14.txt','r')
#f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
#str = repr(f.readline())
#print(str)
#print(f.readlines())
str = f.read()
print(len(str))
print('第一次读：'+str)
print('第二次读：'+f.read())
#如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
#from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
#seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
#seek(x,1) ： 表示从当前位置往后移动x个字符
#seek(-x,2)：表示从文件的结尾往前移动x个字符
#f.seek(0,0)


#f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。
num = f.tell()
print(num)

f.seek(0,0)

print('第三次读：'+f.read())


f.close()

with open('text14.txt','r') as f:
        readData = f.read()
        print("with语法："+readData)
f.close()


#pickle 模块
import pickle
data1 = {'word':'填下',
            'nums':[1,2,3,4,5],
            'num':2,
    'type':None}

selfref_list = [1,2,3]
selfref_list.append(selfref_list)
num = '123113'

f = open('data.pkl','w')

# Pickle dictionary using protocol 0.
pickle.dump(data1,f)
# Pickle the list using the highest protocol available.
pickle.dump(selfref_list,f,-1)

pickle.dump(num,f,0)

f.close()

import pprint
pkl_file = open('data.pkl','r')
data1 = pickle.load(pkl_file)

print('数据1：')
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
print('数据2：')

pprint.pprint(data2)
print('数据3：')
data3 = pickle.load(pkl_file)
#pprint.pprint(pkl_file.read())

pprint.pprint(data3)

pkl_file.close()
