#!/usr/bin/env python
# -*- coding:utf-8 -*-
old_dict = {
    "#1":{'hostname':'c1','cpu_count':2,'mem_capicity':80},
    "#2":{'hostname':'c1','cpu_count':2,'mem_capicity':80},
    "#3":{'hostname':'c1','cpu_count':2,'mem_capicity':80},
             }

new_dict = {
    "#1":{'hostname':'c1','cpu_count':'2','mem_capicity':800},
    "#2":{'hostname':'c2','cpu_count':'2','mem_capicity':80},
    "#4":{'hostname':'c1','cpu_count':'2','mem_capicity':80}
}
old = set(old_dict.keys())
new = set(new_dict.keys())

update_set = old.intersection(new)
#print(update_set)
delete_set = old.symmetric_difference(update_set)
add_set = new.symmetric_difference(update_set)


print(delete_set)
#print(add_set)