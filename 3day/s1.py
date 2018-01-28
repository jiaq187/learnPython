#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''l1 = []
l2 = list()
s1 = set(['alex','liming','xiaohong','alex'])
#print(s2)
#s1.add('alex')
print(s1)
'''


s1 = set(['alex','liming','xiaohong','tony','liming'])
print(s1)

s2 = s1.difference_update('alex','lim   ing')
#2 = s1.remove('tony')
print(s2)