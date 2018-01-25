#!/usr/bin/env python
# -*- coding:utf-8 -*-
lucky_num = 19
retry_count = 0
while  retry_count <3:
    num = int(input("please input a num:"))
    if num > lucky_num:
        print("the guess num is bigger than 6！！")
    elif num < lucky_num:
        print("the guess num is lesser than 6!!")
    else:
        print("bingo!!!")
        break
    retry_count += 1
else:
    print("too many reties!!!")