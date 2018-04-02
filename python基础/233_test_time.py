#! /usr/bin/env python
# -*- coding: utf-8 -*-


import time;
#时间间隔是以秒为单位的浮点小数。
#每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
ticks = time.time()
print('当前时间:'+str(ticks))

localtime = time.localtime(ticks)
#time.struct_time(tm_year=2018, tm_mon=3, tm_mday=23, tm_hour=15, tm_min=5, tm_sec=54, tm_wday=4, tm_yday=82, tm_isdst=0)
print('当前时间:'+str(localtime))
print('%s年%s月%s日%s时%s分%s秒 星期%s 一年的第%s天 是否是夏令时%s'%(localtime[0],localtime[1],localtime[2],localtime[3],localtime[4],localtime[5],localtime[6],localtime[7],localtime[8]))
#获取格式化的时间
#你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():
geshihua = time.asctime(localtime)
print('格式化时间1:'+ str(geshihua))


geshihua2 = time.strftime('%Y-%m-%d  %H:%M:%S',time.localtime())
geshihua3 = time.strftime('%y-%m-%d  %H:%M:%S',time.localtime())
print('格式化时间2:'+geshihua2)
print('格式化时间3:'+geshihua3)

# 格式化成Fri Mar 23 15:11:30 2018形式
print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a,'%a %b %d %H:%M:%S %Y')))

#python中时间日期格式化符号：
#%y 两位数的年份表示（00-99）
#%Y 四位数的年份表示（000-9999）
#%m 月份（01-12）
#%d 月内中的一天（0-31）
#%H 24小时制小时数（0-23）
#%I 12小时制小时数（01-12）
#%M 分钟数（00=59）
#%S 秒（00-59）
#%a 本地简化星期名称
#%A 本地完整星期名称
#%b 本地简化的月份名称
#%B 本地完整的月份名称
#%c 本地相应的日期表示和时间表示
#%j 年内的一天（001-366）
#%p 本地A.M.或P.M.的等价符
#%U 一年中的星期数（00-53）星期天为星期的开始
#%w 星期（0-6），星期天为星期的开始
#%W 一年中的星期数（00-53）星期一为星期的开始
#%x 本地相应的日期表示
#%X 本地相应的时间表示
#%Z 当前时区的名称
#%% %号本身

