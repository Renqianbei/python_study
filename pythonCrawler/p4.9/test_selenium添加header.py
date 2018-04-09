

from  selenium import  webdriver
options = webdriver.FirefoxOptions()
options.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) '
                     'AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
browser = webdriver.Firefox(options=options,executable_path='/Users/renqianbei/Desktop/programing/python/geckodriver')

browser.get('https://www.baidu.com')