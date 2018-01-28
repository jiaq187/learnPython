#!/usr/bin/env python
# -*- coding:utf-8 -*-
f = open('test.log','r+')
'''#f.write('alex\n')
#f.write("贾强")
#ret = f.read(3)
f.seek(1) #指定当前指针位置
print(f.tell()) #查看当前指针位置

f.read(2)
print(f.tell())
f.close()

#print(ret)
'''
f.seek(5)
#print(f.read())
f.truncate()
f.close()