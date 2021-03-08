#! /bin/bash

__author__ = 'zzj'
'''
题目：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
'''
A = open('A.txt')
a = A.read()
A.close()
B = open('B.txt')
b = B.read()
B.close()

C = open('C.txt', 'w')
C.write(a + b)
C.close()

C = open('C.txt')
print(C.read())
C.close()