#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
from urllib import parse
import time
import json
import hashlib
baseurl = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
              

def fanyi(word):
    
#    t = word
#    i =  int(time.time()*1000)
#    o = ('fanyideskweb' + str(t) + str(i) + 'ebSeFb%=XZ%T[KZ)c(sy!').encode('utf-8')
#    o = hashlib.md5(o).hexdigest()

    FormData = {}
    FormData['i'] = word
    FormData['from'] = 'AUTO'
    FormData['to'] = 'AUTO'
    FormData['smartresult'] = 'dict'
    FormData['client'] = 'fanyideskweb'
#    FormData['salt'] = i
#    FormData['sign'] = o
    FormData['doctype'] = 'json'
    FormData['version'] = '2.1'
    FormData['keyfrom'] = 'fanyi.web'
    FormData['action'] = 'FY_BY_CL1CKBUTTON'
    FormData['typoResult'] = 'true'
#使用urlencode方法转换标准格式
    data  = parse.urlencode(FormData).encode('utf-8')
    response = request.urlopen(baseurl,data)
    info = response.info()
    content = response.read()
#    print(info)
#    print(content)

    result = json.loads(content)
    print(result)
    fanyiValues = result['translateResult']
    print('翻译结果:')
    for value in fanyiValues:
        fanyiv = value[0]['tgt']
        print(fanyiv)


while True:
    word = input('请输入：')
    if len(word) > 0:
        fanyi(word)
    else:
        break
