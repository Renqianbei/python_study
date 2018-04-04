import chardet
import  urllib
from urllib import  request

if __name__ == "__main__":

    req = request.Request('http://www.xicidaili.com/')
    req.add_header('User-Agent', 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) '
                                 'AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19')
    response = urllib.request.urlopen(req)

    html = response.read()
    bianma = chardet.detect(html)
    result = html.decode(bianma['encoding'])
    print(bianma)
    print(result)
