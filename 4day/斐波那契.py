#!/usr/bin/env python
# -*- coding:utf-8 -*-
def func(arg1,arg2,stop):
    if arg1 == 0:
        print(arg1,arg2)
    arg3 = arg1 + arg2
    print(arg3)
    if arg3 < stop:
        func(arg2,arg3,stop)
func(0,1,300)