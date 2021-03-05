#! /bin/bash

__author__ = 'zzj'
'''
题目：列表排序及连接
'''
if __name__ == '__main__':
    a = [1, 3, 2]
    b = [3, 4, 5]
    a.sort()  # 对列表 a 进行排序
    print(a)

    # 连接列表 a 与 b
    print(a + b)

    # 连接列表 a 与 b
    a.extend(b)
    print(a)
