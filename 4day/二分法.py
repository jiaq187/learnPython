#!/usr/bin/env python
# -*- coding:utf-8 -*-
def binary_search(data_source,find_n):
    mid = int(len(data_source)/2)
    if len(data_source) >= 1:
        if data_source[mid] > find_n:
            print("data in left of [%s]" %data_source[mid])
            binary_search(data_source[:mid],find_n)
        elif data_source[mid] < find_n:
            print("data in right of [%s]" %data_source[mid])
            binary_search(data_source[mid:],find_n)
        else:
            print("find this number",data_source[mid])
    else:
        print("cannot find")
if __name__ == '__main__':
    data = list(range(1,6000000))
    binary_search(data,1)