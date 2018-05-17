#/usr/bin/env python
# -*- coding:utf-8 -*-
#import collections
'''
有序字典
dic = collections.OrderedDict()
dic['k1'] = 'v1'
dic['k2'] = 'v2'
dic['k3'] = 'v3'
dic.move_to_end('k1')
print(dic)
dic.popitem()
print(dic)
dic.pop('k2')
print(dic)

#2默认字典
 #创建类，defaultdict
MytupleClass = collections.namedtuple('MytupleClass',['x','y','z'])
obj =  MytupleClass(11,22,33)
print(help(obj))
print(obj.x)
print(obj.y)
print(obj.z)

#3双向队列
d = collections.deque()
d.append('1')
d.append('10')
d.append('1')
d.pop()
d.reverse()
d.rotate()
print(d)

#4单项队列
'''
import queue
q = queue.Queue()
q.put('13')
q.put('678')
print(q.qsize())
print(q.get())






