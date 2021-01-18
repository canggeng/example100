#! /bin/bash

__author__ = 'zzj'
'''
题目：练习函数调用。
'''


def hello_runoob():
    print('RUNOOB')


def hello_runoobs():
    for i in range(3):
        hello_runoob()


if __name__ == '__main__':
    hello_runoobs()
