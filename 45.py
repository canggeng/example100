#! /bin/bash

__author__ = 'zzj'

from functools import reduce

'''
题目：统计 1 到 100 之和。
'''

l = range(1, 101)

print(reduce(lambda x, y: x+y, l))

print(sum(l))


##########################################
tmp = 0
for i in range(1,101):
    tmp += i
print ('The sum is %d' % tmp)