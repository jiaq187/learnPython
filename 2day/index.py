#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''#import sys
#print(sys.argv)
t1 = (1,2,{'k1':'v1'})
t1[2]['k1'] = 2
print(t1)
l1 = list
'''
'''
li = [11,22,33,44,55,]
#ret = li.pop(1)
#ret = li.remove(3)
#ret = li.reverse()
#ret = li.append(66)
l1 = [11,13,14,]
tu = tuple(l1)
#print(tu)


l = dict(k1='v1',k2='v2')
new_l = l.fromkeys(['k1','k2','k3'],'v1')
print(new_l)



dic = {'k1':'v1','k2':'v2'}
#print(dic['k1'])
#print(dic['k2'])
#print(dic.get('k3','alex'))

print(dic.keys())
print(dic.values())
print(dic.items())
'''
#dic = {'k1':'v1','k2':'v2'}

#dic.pop('k1')
#dic.setdefault('k4',123)
#dic.popitem()
#dic.update({'k3':123})
#print(dic)
dic = {}
#l1 = []
#l2 = []
li = [11,22,33,44,55,66,77,88,99,90]
for i in li:
    if i>66:
        if "k1" in dic.keys():
            dic['k1'].append(i)
        else:
            dic['k1'] = [i,]
    else:
        if 'k2' in dic.keys():
            dic['k2'].append(i)
        else:
            dic['k2'] = [i,]
#dic['k1'] = l1
#dic['k2'] = l2
    print(dic)

