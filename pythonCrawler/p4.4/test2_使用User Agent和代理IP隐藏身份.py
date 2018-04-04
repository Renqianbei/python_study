# 四、IP代理的使用
#
# 1.为何使用IP代理
#
# 程序的运行速度是很快的，如果我们利用一个爬虫程序在网站爬取东西，
# 一个固定IP的访问频率就会很高，这不符合人为操作的标准，因为人操作不可能在几ms内，
# 进行如此频繁的访问。所以一些网站会设置一个IP访问频率的阈值，
# 如果一个IP访问频率超过这个阈值，说明这个不是人在访问，而是一个爬虫程序。
# 一个很简单的解决办法就是设置延时，但是这显然不符合爬虫快速爬取信息的目的，所以另一种更好的方法就是使用IP代理。使用代理的步骤：
#
# 3.代理IP选取
#
#     在写代码之前，先在代理IP网站选好一个IP地址，推荐西刺代理IP。
#
#     URL：http://www.xicidaili.com/
#
#     注意：当然也可以写个正则表达式从网站直接爬取IP，但是要记住不要太频繁爬取，加个延时什么的，
# 太频繁给服务器带来压力了，
# 服务器会直接把你block，不让你访问的，我就被封了两天。
#
#     从西刺网站选出信号好的IP，我的选择如下：(106.46.136.112:808)

# 编写代码访问http://www.whatismyip.com.tw/，该网站是测试自己IP为多少的网址，服务器会返回访问者的IP。

from urllib import  request
import  socket
if __name__ == '__main__':
    # #访问地址
    url = 'http://www.whatismyip.com.tw/'
    # #代理ip
    # proxy = {'http':'112.239.90.159:61234'}
    # #创建proxyhander
    # prox_support = request.ProxyHandler(proxy)
    # # 创建Opener
    # opener = request.build_opener(prox_support)
    # opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    # #安装OPener
    # request.install_opener(opener)
    #使用资金安装好的Opener
    response = request.urlopen(url)
    #读取信息
    html = response.read().decode('utf-8')
    print('结果')
    print(html)