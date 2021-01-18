#! /bin/bash

__author__ = 'zzj'
'''
题目：按逗号分隔列表。
'''
init_list = ['a', 'b', 'c', 'd', 'e']

for i in init_list:
    print(i, end=',')

##################################
L = [1, 2, 3, 4, 5]
s1 = ','.join(str(n) for n in L)
print(s1)
