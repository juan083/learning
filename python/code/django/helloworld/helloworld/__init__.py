# 固定写法
import pymysql

# 指定mysql clien版本，防止报错：
# django.core.exceptions.ImproperlyConfigured: mysqlclient 1.4.0 or newer is required; you have 0.10.1.
pymysql.version_info = (1, 4, 13, "final", 0)

pymysql.install_as_MySQLdb()  # 告诉django用pymysql代替mysqldb连接数据库