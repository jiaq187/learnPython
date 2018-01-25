#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
f = open("test.log","r")

f.write("this is first line\n")
f.write("this is second line\n")
f.write("this is 3 line\n")

for line in f:
    if "3" in line:
        print("this is the 3 line")
    else:
        print(line)

f = open("test.log","a")
f.write("6\n")
f.write("7\n")
f.write("8\n")
f.write("9\n")
f.close()
'''
f = open("test.log","w+")
f.write("new line\n")
print(f.read())
print(f.readline())