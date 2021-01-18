#! /bin/bash

__author__ = 'zzj'
'''
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
'''


def rever_print(chars):
    l = len(chars)
    if l == 1:
        print(chars, end='')
    else:
        print(chars[l - 1], end='')
        rever_print(chars[:-1])


chars = input('请输入字符')
rever_print(chars)


#################################################
def output(s, l):
    if l == 0:
        return
    print(s[l - 1])
    output(s, l - 1)


s = input('Input a string:')
l = len(s)
output(s, l)
