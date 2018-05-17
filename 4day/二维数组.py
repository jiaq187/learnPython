#!/usr/bin/env python
# -*- coding:utf-8 -*-
data = [[col for col in range(4)]for row in range(4)]
'''
[0, 1, 2, 3]
[0, 1, 2, 3]
[0, 1, 2, 3]
[0, 1, 2, 3]
'''
for i in range(len(data)):
    a = [data[i][i] for row in range(4)]
    print(a)