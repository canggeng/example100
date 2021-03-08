#! /bin/bash

__author__ = 'zzj'
'''
题目：时间函数举例3。
'''
import time
# python3.8以后取消clock
start = time.clock()
for i in range(10000):
    print(i)
end = time.clock()
print('different is %6.3f' % (end - start))
