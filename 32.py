#! /bin/bash

__author__ = 'zzj'
'''
题目：按相反的顺序输出列表的值。
'''

init_list = ['a', 'b', 'c', 'd', 'e']

rev_list = list(reversed(init_list))

print(rev_list)


###########################################
a = ['one', 'two', 'three']
for i in a[::-1]:
    print (i)