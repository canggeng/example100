#! /bin/bash
__author__ = 'zzj'

'''
题目：暂停一秒输出。
'''
from time import sleep

i = 1
while True:
    print(i)
    sleep(1)
    i += 1

