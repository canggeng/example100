#! /bin/bash

__author__ = 'zzj'
'''
题目：学习使用按位或 | 。
'''

if __name__ == '__main__':
    a = 0o75
    b = a | 3
    print ('a | b is %d' % b)
    b |= 7
    print ('a | b is %d' % b)