#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import pymysql

# ip, user, password, dbname
conn = pymysql.connect('127.0.0.1', 'root', '12345678', 'test')

# 游标对象
cursor = conn.cursor()

try:
    cursor.execute('delete from user where id=6')
    # commit是conn，连接commit
    conn.commit()
except:
    print('error')

conn.close()
