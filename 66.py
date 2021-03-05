#! /bin/bash

__author__ = 'zzj'
'''
题目：输入3个数a,b,c，按大小顺序输出。
'''

print("输入3个数a,b,c，按大小顺序输出")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a < b:
    a, b = b, a

if a < c:
    a, c = c, a

if b < c:
    b, c = c, b

print(f"三个数字从小到大为：{a},{b},{c}")
