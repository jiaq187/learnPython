#!/usr/bin/env python
# -*- coding:utf-8 -*-
def login(func):
    def inner(arg):
        print("passwd user vertification....")
        func(arg)
    return inner
@login
def home(name):
    print("Welcome [%s] to home page " % name)
@login
def tv(name):
    print("Welcome [%s] to tv page " % name)
@login
def movie(name):
    print("Welcome [%s] to movie page " % name)




#tv = login(tv)#这行等同于@login
movie('alix')