#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

sender = 'liuhaohao@haokeduo.com'
recevers = ['731846806@qq.com']

#第三方SMTP服务
mail_host = 'smtp.exmail.qq.com'
mail_user = 'liuhaohao@haokeduo.com'
mail_pass = 'W123abc'

#message = MIMEText('我的python发送邮件测试。。。','plain','utf-8')
#创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header('你大爷','utf-8')
message['To'] = Header('收件人哟','utf-8')

message['Subject'] = Header('这是一qfqf封邮件测试内容','utf-8')

#邮件正文
message.attach(MIMEText('我的python发送邮件测试。。。','plain','utf-8'))

#fatherDir = sys.path[0]
#当前文件的绝对路径
filepath = os.path.realpath(sys.argv[0])
#附件1
att1 = MIMEText(open(filepath,'rb').read(),'base64','utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="helle.py"'
message.attach(att1)


try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender,recevers,message.as_string())
    print('邮件发送成功')
except  smtplib.SMTPException as error:
    print(error)
    print('邮件发送失败')
