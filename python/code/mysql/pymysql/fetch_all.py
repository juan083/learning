#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import pymysql

# ip, user, password, dbname
conn = pymysql.connect('127.0.0.1', 'root', '12345678', 'test')

# 游标对象
cursor = conn.cursor()

try:
    cursor.execute('select * from user')
    # rowcount: 获取总记录数
    # fetchall: 多行记录
    # fetchone: 单行记录
    totalCount = cursor.rowcount
    print(totalCount)
    if totalCount > 0:
        result = cursor.fetchall()
        for val in result:
            print(val)
except:
    print('error')

conn.close()
