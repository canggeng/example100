#! /bin/bash

__author__ = 'zzj'
'''
题目：打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
'''
space = ' '
mark = '*'
inline_num = 13
lines = 13
half_lines = lines // 2

for i in range(half_lines + 1):
    for j in range(half_lines - i):
        print(space, end='')
    for k in range((i * 2 + 1)):
        print(mark, end='')
    print('')

for i in range(half_lines):
    for j in range(i+1):
        print(space, end='')
    for k in range(inline_num - (i + 1) * 2):
        print(mark, end='')
    print('')

##########################################################
from sys import stdout

for i in range(4):
    for j in range(2 - i + 1):
        stdout.write(' ')
    for k in range(2 * i + 1):
        stdout.write('*')
    print('')

for i in range(3):
    for j in range(i + 1):
        stdout.write(' ')
    for k in range(4 - 2 * i + 1):
        stdout.write('*')
    print('')
