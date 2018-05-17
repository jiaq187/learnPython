#!/usr/bin/env python
# -*- coding:utf-8 -*-
lucky_num = 19
for i in range(3):
    num = int(input("please input a num:"))
    if num > lucky_num:
        print("the guess num is bigger than 19！！")
    elif num < lucky_num:
        print("the guess num is lesser than 19!!")
    else:
        print("bingo!!!")
        break
else:
    print("too many reties!!!")