#!/usr/bin/python3
# -*- coding:UTF-8 -*-

'''
list的9种不同用途的公用方法
append()，在列表后面增加对象
count()，统计列表中，某个元素的个数
extend()，将一个序列对象转换成列表，并增加到该列表后面
index()，返回查找值的第一个下标，如果查找不到，则抛出错误
insert()，插入对象到指定的下标后面
pop()，弹出列表指定下标的元素，不指定下标，则弹出最后一个元素
remove()，删除列表指定的值，有个多值，则删除第一个
reverse()，反转列表
sort()，排序
'''

list = ['a', 'b', 'c']

# append()，在列表后面增加对象
# ['a', 'b', 'c', 'a']
list.append('a')
print(list)

# count()，统计列表中，某个元素的个数
# 2
count = list.count('a')
print(count)

# extend()，将一个序列对象转换成列表，并增加到该列表后面
# ['a', 'b', 'c', 'a', 'c', [1, 2, 3]]
list.extend(['c', [1, 2, 3]])
print(list)

# index()，返回查找值的第一个下标，如果查找不到，则抛出错误
# 2
i = list.index('c')
print(i)

# insert()，插入对象到指定的下标后面
# ['a', 'meng', 'b', 'c', 'a', 'c', [1, 2, 3]]
list.insert(1, 'meng')
print(list)

# pop()，弹出列表指定下标的元素，不指定下标，则弹出最后一个元素
# ['a', 'b', 'c', 'a', 'c', [1, 2, 3]]
list.pop(1)
print(list)

# remove()，删除列表指定的值，有个多值，则删除第一个
# ['a', 'b', 'a', 'c']
list.remove('c')
list.remove([1, 2, 3])
print(list)

# reverse()，反转列表
# ['c', 'a', 'b', 'a']
list.reverse()
print(list)

# sort()，排序
# ['a', 'a', 'b', 'c']
list.sort()
print(list)
