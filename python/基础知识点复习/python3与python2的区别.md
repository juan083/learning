python3与python2的区别
====

### 区别-总结
1. print函数
2. 整数相除
3. Unicode
4. 异常处理
5. xrange
6. map函数
7. 不支持has_key方法
8. input接收客户端输入str
9. 打开文件
10. 数据类型
11. 模块改名
12. dict的keys

#### 1. print函数
Python3中print为一个函数，必须用括号括起来；Python2是语句

如果 Python2.x 版本想使用使用 Python3.x 的 print 函数，可以导入 __future__ 包，该包禁用 Python2.x 的 print 语句，采用 Python3.x 的 print 函数

#### 2. 整数相除
在Python 2中，3/2的结果是整数，在Python 3中，结果则是浮点数

#### 3. Unicode
- Python 2有两种字符串类型：str和unicode，需在文件头部声明`# -*- coding: utf-8 -*-`

- Python 3中的字符串默认就是Unicode，不需要声明

#### 4. 异常处理
`except ZeroDivisionError, e:` 改变 `except ZeroDivisionError as e`

Python 3中不再支持前一种语法，必须使用as关键字。

#### 5. xrange
range 与 xrange（python3没有xrange）
- 原 : range( 0, 4 )   结果 是 列表 [0,1,2,3 ]
- 改为：list( range(0,4) )

- 原 : xrange( 0, 4 )    适用于 for 循环的变量控制
- 改为：range(0,4)

#### 6. map函数
在Python 2中，map函数返回list，而在Python 3中，map函数返回iterator。

#### 7. 不支持has_key方法
Python 3中的字典不再支持has_key方法

#### 8. input接收客户端输入str
Python3中input得到的为str；

Python2的input的到的为int型，Python2的raw_input得到的为str类型

#### 9. 打开文件
原： file( ..... ) 或 open(.....)
改为：只能用 open(.....)

#### 10. 数据类型
- 去掉long，只保留int，但范围与python2的long一样
- 在python3有了Unicode（UTF-8）字符串，以及一个字节类：byte、bytearrays

#### 11. 模块改名
删减了几个不常用或重复的功能，并将几个模块改名，如：将urllib2、urlparse、robotparse并入urllib模块

#### 12. dict的keys
- python2 返回list
- python3 返回迭代对象，需使用list()转化为列表

### python3.7 新增功能(2018.6.27发布)
1. 强制utf-8运行时模式
2. 具有纳秒分辨率的新时间函数
```
time.clock_gettime_ns()
time.clock_settime_ns()
time.time_ns()
```
3. 内置breakpoint()
breakpoint()可以使函数被调用时让执行中断然后切换到调试器
