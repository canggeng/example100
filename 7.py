#! /bin/bash
__author__ = 'zzj'

'''
题目：将一个列表的数据复制到另一个列表中。
'''

list_a = [1, 2, 3, 4, 5]


def method_a():
    list_b = []
    for i in list_a:
        list_b.append(i)
    print(list_b)


def method_b():
    list_b = list_a.copy()
    print(list_b)


def method_c():
    list_b = [i for i in list_a]
    print(list_b)


method_a()
method_b()
method_c()

##############################
a = [1, 2, 3]
b = a[:]
print(b)
