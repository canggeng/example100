#! /bin/bash
__author__ = 'zzj'
'''
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
'''


def factor(n):
    result = [1]
    for j in range(2, n):
        if n % j == 0:
            result.append(j)

        if n == 1:
            break
    sum_n = sum(result)
    if n == sum_n and n != 1:
        return True
    else:
        return False


for i in range(1, 1001):
    if factor(i):
        print(f"{i}是完数")

################################################################

from sys import stdout

for j in range(2, 1001):
    k = []
    n = -1
    s = j
    for i in range(1, j):
        if j % i == 0:
            n += 1
            s -= i
            k.append(i)

    if s == 0:
        print(j)
        for i in range(n):
            stdout.write(str(k[i]))
            stdout.write(' ')
        print(k[n])
