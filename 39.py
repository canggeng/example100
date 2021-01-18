#! /bin/bash

__author__ = 'zzj'
'''
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
'''


sort_lsit = [4123, 5345, 21344, 645, 32, 1, 56634, 87, 44, 42]
a = int(input("请输入一个整数："))

sort_lsit.append(a)

sort_lsit.sort()
print(sort_lsit)



#########################################
if __name__ == '__main__':
    # 方法一 ： 0 作为加入数字的占位符
    a = [1,4,6,9,13,16,19,28,40,100,0]
    print ('原始列表:')
    for i in range(len(a)):
        print (a[i])
    number = int(input("\n插入一个数字:\n"))
    end = a[9]
    if number > end:
        a[10] = number
    else:
        for i in range(10):
            if a[i] > number:
                temp1 = a[i]
                a[i] = number
                for j in range(i + 1,11):
                    temp2 = a[j]
                    a[j] = temp1
                    temp1 = temp2
                break
    print ('排序后列表:')
    for i in range(11):
        print (a[i])