#!/usr/bin/env python
# -*- coding:utf-8 -*-
name = input("name:").strip()
age = int(input("age:"))
job = input("job:").strip()
'''
.strip()脱去空格
print("Information of []:" + name +"\nName:[]"+name+"\nAge:[]"+age+"\njob:[]"+job+"")
print("Information of %s:\nName:%s\nAge:%s\nJob:%s" %(name,name,age,job))
%d 
%f
'''
msg = '''
InforMation of %s
name:%s
age:%s
job:%s
'''%(name,name,age,job)
print(msg)
