#! /bin/bash

__author__ = 'zzj'
'''
题目：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。
'''
if __name__ == '__main__':
    while True:
        n = int(input("请输入数字： "))
        s = ''
        if 1 > n or n > 50:
            continue
        for i in range(n):
            s += '*'
        print(s)

###############################
    n = 1
    while n <= 7:
        a = int(input('input a number:\n'))
        while a < 1 or a > 50:
            a = int(input('input a number:\n'))
        print(a * '*')
        n += 1