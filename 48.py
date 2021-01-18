#! /bin/bash

__author__ = 'zzj'
'''
题目：数字比较。
'''
while True:
    x = int(input("请输入数字x："))
    y = int(input("请输入数字y："))

    if x > y:
        print(f"{x}大于{y}")
    elif x == y:
        print(f"{x}等于{y}")
    else:
        print(f"{x}小于{y}")

###################################################
if __name__ == '__main__':
    i = 10
    j = 20
    if i > j:
        print('%d 大于 %d' % (i, j))
    elif i == j:
        print('%d 等于 %d' % (i, j))
    elif i < j:
        print('%d 小于 %d' % (i, j))
    else:
        print('未知')
