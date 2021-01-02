#! /bin/bash
import math

__author__ = 'zzj'
'''
题目：判断101-200之间有多少个素数，并输出所有素数。
'''

prime = 0

for i in range(101, 201):
    prime = 0
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            prime = 1
            break
    if prime == 0:
        print(f"{i}是素数")

