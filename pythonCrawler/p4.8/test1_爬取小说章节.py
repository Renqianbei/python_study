import  urllib
from  urllib import request
import  chardet
from  bs4 import  BeautifulSoup

#获取指定小说链接下的所有章节地址 依次下载
def downloadXiaoshuo():
    baseurl = 'http://www.biqukan.com/1_1094/'
    response = request.urlopen(baseurl)
    result = response.read()
    coding = chardet.detect(result)
    html = result.decode(coding["encoding"])
    # 创建soup对象
    soup = BeautifulSoup(html, 'lxml')

    listmain = soup.find_all(class_='listmain')
    print(type(listmain))
    # 查询的结果创建一个新的soup
    soup = BeautifulSoup(str(listmain), 'lxml')
    # print(soup.prettify())
    beginLoad = False
    # print(soup.dl.contents)
    for child in soup.dl.children:

        if child != '\n':

            if beginLoad:
                if child.a != None:
                    title = child.string
                    loadurl = 'http://www.biqukan.com' + child.a['href']
                    print(title + '地址:' + loadurl)
                    loadfile(title,loadurl)

                continue
            if '正文卷' in child.string:
                beginLoad = True

#解析具体章节内容 写入本地文件中
def loadfile(title = '第x章',download_url  = "http://www.biqukan.com/1_1094/5403177.html"):

     head = {}
     head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
     req = request.Request(download_url,headers=head)
     response = request.urlopen(req)
     html = response.read().decode('gbk','ignore')
     soup = BeautifulSoup(html,'lxml')
     txts = soup.find_all('div',class_ = 'showtxt')
     soup = BeautifulSoup(str(txts),'lxml')
     with open('一念永恒.txt','a',encoding='utf-8') as  f:
         f.write('\n%s\n'%title)
         f.write(soup.div.text)



downloadXiaoshuo()