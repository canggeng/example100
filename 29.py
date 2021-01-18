#! /bin/bash

__author__ = 'zzj'
'''
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
'''


def rev_chars(chars, l):
    new_chars = ''
    for i in range(l):
        new_chars += chars[l - i - 1]
    return new_chars


chars = input('请输入不多于5位正整数：')
try:
    a = int(chars)
    l = len(chars)
    if l > 5:
        print("输入位数过多")
        exit(0)

    print(f"它是一个{l}位数")

    print(rev_chars(chars, l))

except ValueError as e:
    print("请输入5位正整数")
    exit(0)


###########################################
x = int(input("请输入一个数:\n"))
a = x // 10000
b = x % 10000 // 1000
c = x % 1000 // 100
d = x % 100 // 10
e = x % 10

if a != 0:
    print("5 位数：", e, d, c, b, a)
elif b != 0:
    print("4 位数：", e, d, c, b)
elif c != 0:
    print("3 位数：", e, d, c)
elif d != 0:
    print("2 位数：", e, d)
else:
    print("1 位数：", e)