#!/usr/bin/env python
# -*- coding:utf-8 -*-
def test():
    try:
        x = int(input("plz input a num:"))
        y = int(input("plz input a num:"))
        num = x / y
    except Exception as e:
        print("valid value:",e)
    else:
        print(num)
test()
