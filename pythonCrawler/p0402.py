#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from  urllib import  request
from  urllib  import  error
import  urllib

#re 正则库
import re
import os
import sys

#获取内容
def gethtmlContent(url):
    
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    return html



# 从html中解析出所有jpg图片的url
# 百度贴吧html中jpg图片的url格式为：<img ... src="XXX.jpg" width=...>
def getJPGs(html):
    jpgReg = re.compile(r'<img.+?src="(.+?\.jpg)"' )  # 注：这里最后加一个'width'是为了提高匹配精确度
    #解析出jpg的url列表
    jpgs = re.findall(jpgReg,html)
    return jpgs


#下载图片 保存成指定文件名
def downloadjpg(imageurl,fileName):
    try:
        urllib.request.urlretrieve(imageurl,fileName)
    except  error.HTTPError as err:
        print('下载发生错误:%s',err.code)
        raise
    except  error.URLError as err:
         print('错误%s',err.reason)
         raise
    except  ValueError as err:
        print('错误%s',err)
        raise


def batchDownloadJpgs(imageurls,path = './Imags'):
    count = 1
    if not os.path.exists(path):
        os.system('mkdir %s'%path)
    for url in imageurls:
        try:
            downloadjpg(url,path + '/' + str(count) + '.jpg')
            print('下载完第%d张'%count)
        except:
            pass
        count = count+1

def download(url):
    print('开始获取内容')
    html = gethtmlContent(url)
    print('开始解析图片列表')
    jpgs = getJPGs(html)
    print('开始下载图片')
    batchDownloadJpgs(jpgs)
def  main():
    url = "http://tieba.baidu.com/p/2256306796"
    download(url)



main()

