from  bs4 import  BeautifulSoup
# try:
#     f = open('./testHtml.html', 'r')
#     html = f.read()
# finally:
#     if f:
#         f.close()
#上面太繁琐 可以用with
with open('./testHtml.html', 'r') as f:
    html = f.read()
    # print(html)

#创建soup对象
soup = BeautifulSoup(html,'lxml')
#使用如下代码格式化输出：
print(soup.prettify())


# b)Beautiful Soup四大对象
#
#     Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,所有对象可以归纳为4种:
#
# Tag
# NavigableString
# BeautifulSoup
# Comment
print('分割线==================')
print(soup.title)
# <title>Renqianbei</title>
print(type(soup.title))
# <class 'bs4.element.Tag'>
print(soup.head)
print(soup.a)
# <a class="sister" href="http://blog.csdn.net/c406495762/article/details/58716886" id="link1">Python3网络爬虫(一)：利用urllib进行简单的网页抓取</a>
print(soup.p)
# <p class="title" name="blog"><b>My Blog</b></p>
print(type(soup.name))
print(soup.name)
print(soup.attrs)
#<class 'str'>
#[document]
#{}
print(soup.title.name)
# title
print(soup.a.attrs)
# {'href': 'http://blog.csdn.net/c406495762/article/details/58716886', 'class': ['sister'], 'id': 'link1'}
print(soup.a['class'])
print(soup.a.get('class'))
#['sister']
#['sister']

# 既然我们已经得到了标签的内容，那么问题来了，我们要想获取标签内部的文字怎么办呢？很简单，用.string
# 即可，例如
print(soup.title.string)
# Renqianbei


# comment
print(soup.li)
print(soup.li.string)
print(type(soup.li.string))
#<li><!--注释--></li>
#注释
#<class 'bs4.element.Comment'>
# li标签里的内容实际上是注释，但是如果我们利用 .string 来输出它的内容，我们发现它已经把注释符号去掉了，所以这可能会给我们带来不必要的麻烦。
#
#     我们打印输出下它的类型，发现它是一个 Comment 类型，所以，我们在使用前最好做一下判断，判断代码如下：
from bs4 import element
if type(soup.li.string) == element.Comment:
    print('该元素是注释元素：'+soup.li.string)

# tag的content属性可以将tag的子节点以列表的方式输出：
print(soup.body.contents)
print(soup.body.contents[1])

# children：
#
#     它返回的不是一个 list，不过我们可以通过遍历获取所有子节点，它是一个 list 生成器对象：

for child in soup.body.children:
    print('chidren===============    ',child)

# find_all(name, attrs, recursive, text, limit, **kwargs)：
# 方法搜索当前tag的所有tag子节点, 并判断是否符合过滤器的条件。
#   1）name参数
print(soup.find_all('a'))

# 传递正则表达式：
#
#     如果传入正则表达式作为参数,Beautiful Soup会通过正则表达式的 match() 来匹配内容.下面例子中找出所有以b开头的标签,这表示<body>和<b>标签都应该被找到
import  re
print('正则')
print(soup.find_all(re.compile('^b')))
#
# 传递列表：
#
#     如果传入列表参数，Beautiful Soup会将与列表中任一元素匹配的内容返回，下面代码找到文档中所有<title>标签和<b>标签：
print('传递列表')
print(soup.find_all(['title','b']))

# True 可以匹配任何值,下面代码查找到所有的tag,但是不会返回字符串节点：
print('\n传递 True-=========\n')

for tag in soup.find_all(True):
    print(tag.name)

 # 2)attrs参数
 #
 #    我们可以通过
 #    find_all()
 #    方法的
 #    attrs
 #    参数定义一个字典参数来搜索包含特殊属性的tag。

print(soup.find_all(attrs={"class": "title"}))
# [<p class="title" name="blog"><b>My Blog</b></p>]

# 3)recursive参数
#
#     调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,如果只想搜索tag的直接子节点,可以使用参数 recursive=False。
# 4)text参数
#
#     通过 text 参数可以搜搜文档中的字符串内容，与 name 参数的可选值一样, text 参数接受字符串 , 正则表达式 , 列表, True。

print(soup.find_all(text="Python3网络爬虫(三)：urllib.error异常"))
#['Python3网络爬虫(三)：urllib.error异常']
# 5)limit参数
#
#     find_all() 方法返回全部的搜索结构,如果文档树很大那么搜索会很慢.如果我们不需要全部结果,可以使用 limit 参数限制返回结果的数量.效果与SQL中的limit关键字类似,当搜索到的结果数量达到 limit 的限制时,就停止搜索返回结果。
#
#     文档树中有3个tag符合搜索条件,但结果只返回了2个,因为我们限制了返回数量：

print(soup.find_all("a", limit=2))

# 6)kwargs参数
#
#     如果传入 class 参数,Beautiful Soup 会搜索每个 class 属性为 title 的 tag 。kwargs 接收字符串，正则表达式

print(soup.find_all(class_="title"))
#[<p class="title" name="blog"><b>My Blog</b></p>]