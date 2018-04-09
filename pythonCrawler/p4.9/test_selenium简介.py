
# 首先要下载selenium框架
# 然后去https://github.com/mozilla/geckodriver/releases 下载geckodriver驱动对应火狐浏览器Firefox  mac版本的就去下载  macos  当然还有windows版本

# from  selenium import  webdriver
# browser = webdriver.Chrome()
# browser.get('http://www.baidu.com/')
# 直接执行上面代码会报下面错误  找不到 chromedriver
# selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. 出现问题

#当前环境 selenium Version: 3.11.0  python3  火狐浏览器Firefox 59.0.2 (64 位)
#解决方案
# 将下载的geckodriver放在某个位置，然后
from selenium import webdriver
import time

#指定geckodriver驱动的位置
# 教大家一个方法，我用了在python下执行了help(webdriver.Firefox) 回车，这样就知道了传什么参数。
browser = webdriver.Firefox(executable_path='/Users/renqianbei/Desktop/programing/python/geckodriver')

browser.get('http://www.baidu.com')
time.sleep(5)
print('Browser will close.')
browser.close()
print('Browser is close')





