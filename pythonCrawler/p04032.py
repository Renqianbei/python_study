#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
from urllib import parse
import time
import json
#import hashlib
baseurl = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
              

def fanyi(word):

#注释部分是 抓取过程中 发现有道翻译 的 salt 参数 和  sign参数是经过特殊处理的  所以需要  找到规则写的参数  后来 直接替换了接口 所以这些参数就不需要了
#    t = word
#    i =  int(time.time()*1000)
#    o = ('fanyideskweb' + str(t) + str(i) + 'ebSeFb%=XZ%T[KZ)c(sy!').encode('utf-8')
#md5运算
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
