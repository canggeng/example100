#! /bin/bash

__author__ = 'zzj'
'''
题目：求一个3*3矩阵主对角线元素之和。
'''
matrix = [
    [15, 68, 73],
    [61, 84, 12],
    [99, 12, 76],
]

sum_list = []
for i in range(3):
    for j in range(3):
        if i == j:
            sum_list.append(matrix[i][j])
        elif i == (2 - j):
            sum_list.append(matrix[i][j])

print(sum(sum_list))

###########################################
if __name__ == '__main__':
    a = []
    sum = 0.0
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(float(input("input num:\n")))
    for i in range(3):
        sum += a[i][i]
    print(sum)
