#!/usr/bin/env python
# -*- coding:utf-8 -*-
lucky_num = 6
num = -1
while lucky_num != num:
    num = int(input("please input a num:"))
    if num > lucky_num:
        print("the guess num is bigger than 6！！")
    elif num < lucky_num:
        print("the guess num is lesser than 6!!")
print("bingo!!!")