#!/usr/bin/python3
# -*- coding:UTF-8 -*-

import pymysql

# ip, user, password, dbname
conn = pymysql.connect('127.0.0.1', 'root', '12345678', 'test')

# 游标对象
cursor = conn.cursor()

try:
    cursor.execute('delete from user where id=6')
    # 在Python数据库编程中，当游标建立之时，就自动开始了一个隐形的数据库事务。
    # commit()方法游标的所有更新操作，rollback（）方法回滚当前游标的所有操作
    conn.commit()
except:
    conn.rollback()
    print('error')

conn.close()
