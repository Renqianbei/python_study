import  urllib
from  urllib import request
import chardet
import  re
import  itertools
url  = 'http://www.xicidaili.com'
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 '
                         '(KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
}

req = request.Request(url,headers= headers)

response = request.urlopen(req)

html = response.read()

code = chardet.detect(html)

result = html.decode(code['encoding'])
# print(result)

# <td>[0-9]{1,3}\.[0-9 .]*</td>

pattern = re.compile(r'<td>([0-9.]*)</td>') #ip和端口
#
alls = re.findall(pattern,result)
#
# print(ips)
# alls = re.finditer(pattern,result)
ips = [[],[]]

index = itertools.cycle([0,1])

for value in alls:
    ips[next(index)].append(value)

for i in range(0,len(ips[0])):
    print(ips[0][i] + ':' + ips[1][i])
