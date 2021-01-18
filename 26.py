#! /bin/bash

__author__ = 'zzj'
'''
题目：利用递归方法求5!。
'''


def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))


############################################
def fact(j):
    sum = 0
    if j == 0:
        sum = 1
    else:
        sum = j * fact(j - 1)
    return sum


print(fact(5))
