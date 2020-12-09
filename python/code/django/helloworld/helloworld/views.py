#!/usr/bin/python3
# -*- coding:UTF-8 -*-

from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world ! ")

