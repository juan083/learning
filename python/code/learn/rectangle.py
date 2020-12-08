#!/usr/bin/python3
# -*- coding:UTF-8 -*-

class Rectangle(object):

    width = 0

    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getarea(self):
        return self.width * self.height

    # 必须放置最后，否则报错找不到方面、属性
    area = property(getarea, doc='area')

obj = Rectangle(5, 10)
print(obj.area, obj.doc)
