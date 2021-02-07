#! /bin/bash

__author__ = 'zzj'
'''
题目：取一个整数a从右端开始的4〜7位。
'''

a = int(input("请输入整数a，最少需要7位: "))

a //= 1000

a %= 10000

print(a)


##########################################################
# 完全做错了
if __name__ == '__main__':
    a = int(input('input a number:\n'))
    b = a >> 4
    c = ~(~0 << 4)
    d = b & c
    print ('%o\t%o' %(a,d))