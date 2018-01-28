#!/usr/bin/env python
# -*- coding:utf-8 -*-
def calc(n):
    print(n)
    if n/2 > 1:
        ret = calc(n/2)
        print('ret',ret)
    print('N',n)
    return n
calc(100)