#!/usr/bin/env python
# -*- coding:utf-8 -*-
import collections
'''obj = collections.Counter("isadfdhjfdsaadf")
# elments => 原生的值
#     obj => 

#print(obj)
ret = obj.most_common(4)
#print(ret)
for k in obj.elements():
    print(k)
for k,v in obj.items():
    print(k,v)'''
obj = collections.Counter(['11','22','33','44'])
print(obj)
c = obj.update(22)
print(c)