#! /bin/bash

__author__ = 'zzj'
'''
题目：将一个数组逆序输出。
'''
sort_lsit = [4123, 5345, 21344, 645, 32, 1, 56634, 87, 44, 42]
sort_lsit.sort(reverse=True)
print(sort_lsit)


###############################
if __name__ == '__main__':
    a = [9,6,5,4,1]
    N = len(a)
    print (a)
    for i in range(len(a) // 2):
        a[i],a[N - i - 1] = a[N - i - 1],a[i]
    print (a)