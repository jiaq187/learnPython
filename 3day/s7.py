#!/usr/bin/env python
# -*- coding:utf-8 -*-
#无参数
#show(): ---->show()
#一个参数
'''def show(arg):
    print(arg)
show('kkkkkkk')

#两个参数
def show(arg,xxx):
    print(arg,xxx)
show('djfjd','7898879')

#默认参数,必须放在最后
def show(a1,a2=999):
    print(a1,a2)
show(111)

#指定参数
def show(a1,a2):
    print(a1,a2)
show(a2=123,a1=89666)

#一个*元组 俩个*字典
def show(**arg):
    print(arg,type(arg))
show(n1=11,n2=23)

def show(*args,**kargs):
    print(args,type(args))
    print(kargs,type(kargs))
show(11,22,33,44,n1=9878,alex='sb')

def show(*args,**kargs):
    print(args,type(args))
    print(kargs,type(kargs))
l = [11,22,33,44]
d = {'n1':88,'alex':'sb'}
#show(l,d)
show(*l,**d)
'''
s1 = "{name} is {acter}"
#result = s1.format('alex','2b')
l = ['alex','sb']
d = {'name':'alex','acter':'sb'}
#result = s1.format(*l)
result = s1.format(**d)

print(result)
