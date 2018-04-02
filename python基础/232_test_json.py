#! /usr/bin/env python
# -*- coding: utf-8 -*-


import json

#json.dumps(): 对数据进行编码。
#json.loads(): 对数据进行解码。

studentData = {'name':'mmp',
    'age':2,
    'pic':'www.baidu.com',
    'money':None,
    'addresses':['北京','新加坡','澳门']
}


json_str = json.dumps(studentData)

print('studentData python=======:',studentData)
print(studentData["name"])

print('JSON ========:',json_str)

originData = json.loads(json_str)
print('originData==:',originData)
print(originData["name"])
