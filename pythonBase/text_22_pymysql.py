#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import pymysql


#open
db = pymysql.connect('rqb.local','rqb','123','TESTDB')
#创建游标对象
cursor = db.cursor()

#执行方法
cursor.execute('select version()')
data = cursor.fetchone()
print('数据库版本%s'%data)

# 使用预处理语句创建表
sql = '''CREATE TABLE IF NOT EXISTS Teacher (
    FIRST_NAME  CHAR(20) NOT NULL,
    LAST_NAME  CHAR(20),
    AGE INT,
    SEX CHAR(1),
    INCOME FLOAT )'''
cursor.execute(sql)

#
cursor.execute('show tables')
results = cursor.fetchall()
for row in results:
     print(row)


# SQL 插入语句
sql = "INSERT INTO Teacher(FIRST_NAME, \
LAST_NAME, AGE, SEX, INCOME) \
VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
    ('Mac', 'Mohan', 20, 'M', 2000)
try:
    # 执行sql语句
    cursor.execute(sql)
    # 执行sql语句
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()


# SQL 查询语句
sql = "SELECT * FROM Teacher \
WHERE INCOME > '%d'" % (1000)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
            fname = row[0]
            lname = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            # 打印结果
            print ("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
                   (fname, lname, age, sex, income ))
except:
    print ("Error: unable to fetch data")


db.close()
