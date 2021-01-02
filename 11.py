#! /bin/bash
from time import sleep

__author__ = 'zzj'
'''
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
假如兔子都不死，问每个月的兔子总数为多少？
'''


def rabbit_count():
    first = 1
    second = 0
    third = 0
    while True:
        count = first + second + third
        print(f"兔子总数为：{count}")
        sleep(1)
        born = third + second
        third += second
        second = first
        first = born


rabbit_count()

################################################################
f1 = 1
f2 = 1
for i in range(1, 22):
    print('%12ld %12ld' % (f1, f2), end=" ")
    if (i % 3) == 0:
        print('')
    f1 = f1 + f2
    f2 = f1 + f2
