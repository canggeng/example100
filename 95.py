#! /bin/bash

__author__ = 'zzj'
'''
题目：字符串日期转换为易读的日期格式。
'''
import time

dt = time.strptime("Aug 28 2015 12:00AM", "%b %d %Y %I:%MAM")
print(time.strftime("%Y-%m-%d %H:%M:%S", dt))
