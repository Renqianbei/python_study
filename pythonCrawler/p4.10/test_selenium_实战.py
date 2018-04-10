from  selenium import  webdriver

options = webdriver.FirefoxOptions()
options.add_argument('Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) '
                     'Version/3.0 Mobile/3A101a Safari/419.3')

driver = webdriver.Firefox(options=options,executable_path='../../geckodriver')
#打开网页
driver.get('https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html')

morebtn = driver.find_element_by_xpath('//div/span[@class="moreBtn goBtn"]')
#调用js让视图滚动到 morebtn所在位置
driver.execute_script('arguments[0].scrollIntoView();',morebtn)
# 点击morebtn
morebtn.click()

import time
time.sleep(2)
# #滚动到底部
bottom = driver.find_element_by_xpath('//div[@class="inner"]/div[@id="bottom-download"][@class="bd"]')
print(bottom)
driver.execute_script('arguments[0].scrollIntoView()',bottom)

pagecountElement =driver.find_element_by_xpath('//div[@class="reader-tools-page xllDownloadLayerHit_left"]/span[@class="page-count"]')

totalcount = pagecountElement.text # 值是 '/123'要转换成数字

from  functools import reduce
def f(x):
    i = ord(x)
    if  i>=ord('0') and i<=ord('9'):
        return int(x)
    else:
        return 0

totalcount = reduce(lambda x,y:10*x+y,map(f,totalcount))
print(totalcount)

#要开始抓文档主要内容了
from bs4 import BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html,'lxml')

readerContainer = soup.find_all('div',attrs={'id':'reader-container-inner-1','class':'reader-container-inner'})
print(len(readerContainer))
for  eachReader in readerContainer:
     readsoup = BeautifulSoup(str(eachReader),'lxml')
     contents = readsoup.find_all(class_ = 'mod reader-page complex hidden-doc-banner reader-page-13')
     print('樟树%d'%len(contents))
     for child in contents:
         print(child)
         print(child.name)
         s = BeautifulSoup(str(child), 'lxml')
         ns = s.find_all(class_='ie-fix')
         for result in ns:
             print(result.name)
             print(result.content)

# mod reader-page complex reader-page-1
# mod reader-page complex hidden-doc-banner reader-page-13

