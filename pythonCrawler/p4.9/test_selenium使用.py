from  selenium import  webdriver
from  selenium.webdriver.common.keys import  Keys

driver = webdriver.Firefox(executable_path='/Users/renqianbei/Desktop/programing/python/geckodriver')
driver.get('http://www.python.org')
assert 'Python' in driver.title
#找到搜索输入框元素
elem = driver.find_element_by_name('q')
# 另一种写法
# from  selenium.webdriver.common.by import By
# elem = driver.find_element(By.NAME,'q')
elem.send_keys('pycon')
elem.send_keys(Keys.RETURN)

print(driver.page_source)
# 其中
# driver.get
# 方法会打开请求的URL，WebDriver
# 会等待页面完全加载完成之后才会返回，即程序会等待页面的所有内容加载完成，JS渲染完毕之后才继续往下执行。注意：如果这里用到了特别多的
# Ajax
# 的话，程序可能不知道是否已经完全加载完毕。
# 最后最重要的一点是可以获取网页渲染后的源代码。通过，输出
# page_source
# 属性即可。这样，我们就可以做到网页的动态爬取了。

# 元素选取
#
#     关于元素的选取，有如下API：

# find_element_by_id
# find_element_by_name
# find_element_by_xpath
# find_element_by_link_text
# find_element_by_partial_link_text
# find_element_by_tag_name
# find_element_by_class_name
# find_element_by_css_selector
# 多个元素选取：
# find_elements_by_name
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector

# 3 界面交互
#
#     通过元素选取，我们能够找到元素的位置，我们可以根据这个元素的位置进行相应的事件操作，例如输入文本框内容、鼠标单击、填充表单、元素拖
# 拽等等。由于篇幅原因，我就不一一讲解了，主要讲解本次实战用到的鼠标单击，更详细的内容，可以查看官方文档。
elem = driver.find_element_by_xpath("//a[@data-fun='next']")
elem.click()
# 比如上面这句话，我使用find_element_by_xpath()
# 找到元素位置，暂且不用理会这句话什么意思，暂且理解为找到了一个按键的位置。然后我们使用click()
# 方法，就可以触发鼠标左键单击事件。是不是很简单？但是有一点需要注意，就是在点击的时候，元素不能有遮挡。什么意思？就是说我在点击这个按键之前，窗口最好移动到那里，因为如果这个按键被其他元素遮挡，click()
# 就触发异常。因此稳妥起见，在触发鼠标左键单击事件之前，滑动窗口，移动到按键上方的一个元素位置：
# page = driver.find_elements_by_xpath("//div[@class='page']")
# driver.execute_script('arguments[0].scrollIntoView();', page[-1]) #拖动到可见的元素去

