#!/usr/bin/python3
# -*- coding:UTF-8 -*-

'''
遍历tuple
和list一样
'''

tuple = ('a', 'b', 'c')

for v in tuple:
    # a
    print(v)

for v in iter(tuple):
    # a
    print(v)

for i in range(len(tuple)):
    # 0 a
    print(i, tuple[i])

for item in enumerate(tuple):
    # (0, 'a')
    print(item)