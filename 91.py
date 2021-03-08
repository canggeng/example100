#! /bin/bash

__author__ = 'zzj'
'''
题目：时间函数举例1。
'''
import time

print(time.time())
print(time.ctime(time.time()))
print(time.asctime(time.localtime(time.time())))
print(time.asctime(time.gmtime(time.time())))