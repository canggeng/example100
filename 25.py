#! /bin/bash

__author__ = 'zzj'
'''
题目：求1+2!+3!+...+20!的和。
'''


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


sum = 0
for i in range(1, 21):
    sum += factorial(i)

print(sum)


#############################################
n = 0
s = 0
t = 1
for n in range(1,21):
    t *= n
    s += t
print ('1! + 2! + 3! + ... + 20! = %d' % s)


################################################

s = 0
l = range(1,21)
def op(x):
    r = 1
    for i in range(1,x + 1):
        r *= i
    return r
s = sum(map(op,l))
print ('1! + 2! + 3! + ... + 20! = %d' % s)