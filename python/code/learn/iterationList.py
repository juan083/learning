#!/usr/bin/python3
# -*- coding:UTF-8 -*-

'''
遍历list
'''

list = ['a', 'b', 'c']

for v in list:
    # a
    print(v)

for v in iter(list):
    # a
    print(v)

for i in range(len(list)):
    # 0 a
    print(i, list[i])

for item in enumerate(list):
    # (0, 'a')
    print(item)

print(list.count('a'))
