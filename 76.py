#! /bin/bash

__author__ = 'zzj'
'''
题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
'''


def doit(n):
    sum = 0
    for i in range(n, 0, -2):
        sum += 1 / i
    return sum

n = int(input("请输入n: "))
print(doit(n))