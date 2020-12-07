#!/usr/bin/python3
# -*- coding:UTF-8 -*-

'''
字符串的大小写转换

capitalize，首字符大写
lower，全部转小写
upper，全部转大写
swapcase，大小写互转
title，单词首字母大写，其他小写
'''

str = 'apple Is Fruit.'

# capitalize，首字符大写
# Apple is fruit.
print(str.capitalize())

# lower，全部转小写
# apple is fruit.
print(str.lower())

# upper，全部转大写
# APPLE IS FRUIT.
print(str.upper())

# swapcase，大小写互转
# APPLE iS fRUIT.
print(str.swapcase())

# title，单词首字母大写，其他小写
# Apple Is Fruit.
print(str.title())
