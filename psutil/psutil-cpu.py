#!/usr/bin/env python
# -*- coding:utf-8 -*-
import psutil
for x in range(3):
    y=psutil.cpu_percent(interval=1,percpu=True)
    print(y)
i=psutil.cpu_count()
print(i)
z = psutil.net_connections()
print(z)