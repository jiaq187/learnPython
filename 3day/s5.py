#!/usr/bin/env python
# -*- coding:utf-8 -*-
import copy
'''
#浅拷贝
#copy.copy()
#深拷贝
#copy.deepcopy()
#赋值
a1 = 123123
a2 = 123123
#print(id(a1))
#print(id(a2))

#a3 = copy.deepcopy(a1)
#print(id(a3))

n1 = {"k1":"wu","k2":"123",'k3':["alex",456]}
n2 = n1

#n3 = copy.copy(n1)
n3 = copy.deepcopy(n1)
#print(id(n1))
#print(id(n2))
#print(id(n3))

print(id(n1['k3']))
print(id(n3['k3']))
'''
dic = {
    "cpu":[80,],
    "mem":[80,],
    "disk":[80]
}
print('before',dic)

#new_dic =copy.copy(dic)
new_dic = copy.deepcopy(dic)
new_dic['cpu'][0] = 50
print(dic)
print(new_dic)
