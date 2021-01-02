#! /bin/bash
__author__ = 'zzj'

"""
题目：暂停一秒输出，并格式化当前时间。
"""


from datetime import datetime
from time import sleep

while True:
    n = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(n)
    sleep(1)


########################################################
import time

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# 暂停一秒
time.sleep(1)

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))