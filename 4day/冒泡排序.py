
#!/usr/bin/env python
# -*- coding:utf-8 -*-
data = [10,2,3,54,53,223,45,55,67,76]
for index,i in enumerate(data):
    if i > data[index+1]:
        data[index+1]