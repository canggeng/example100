#! /bin/bash
from functools import reduce
__author__ = 'zzj'

'''
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，
几个数相加由键盘控制。
'''


def spec_sum(num, length):
    result = 0
    pre_digit = 0
    for i in range(length):
        next_digit = num * 10**i + pre_digit
        result += next_digit
        pre_digit = next_digit

    return result


print(spec_sum(2, 5))

########################################################################
# !/usr/bin/python


Tn = 0
Sn = []
n = int(input('n = '))
a = int(input('a = '))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print(Tn)

Sn = reduce(lambda x, y: x + y, Sn)
print("计算和为：", Sn)