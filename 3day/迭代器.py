#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
name = iter(['alex','jack','list'])
print(name.__next__())
print(name.__next__())
print(name.__next__())
print(name.__next__())
'''
def cash_money(amount):
    while amount >0:
          amount -= 100
          yield 100
          print("又来取钱啦！！")
atm = cash_money(500)
#print(type(atm))
print(atm.__next__())
print(atm.__next__())
print("叫个大保健。。。。")
print(atm.__next__())
print(atm.__next__())
print(atm.__next__())

