#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import urllib
from urllib import request

#chardet模块 可以自动识别html是用的什么编码
import chardet

if  __name__ == '__main__':
    
    
#    response = request.urlopen('http://fanyi.baidu.com/')

    req = request.Request('http://fanyi.baidu.com/')
    response = request.urlopen(req)
    
    html = response.read()
    print(response.geturl())
    info = response.info()
    print(type(info))
    print(info)
    print(info['Content-Type'])
    print(response.getcode())
    #content  = html.decode('utf-8')
    #chardet模块 可以自动识别html是用的什么编码
    codeInfo = chardet.detect(html)
    print(codeInfo)
    content = html.decode(codeInfo['encoding'])
#    print(content)

