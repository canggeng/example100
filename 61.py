#! /bin/bash

__author__ = 'zzj'
'''
题目：打印出杨辉三角形
1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
1 5 10 10 5 1 
1 6 15 20 15 6 1 
1 7 21 35 35 21 7 1 
1 8 28 56 70 56 28 8 1 
1 9 36 84 126 126 84 36 9 1
'''

first = 1
upper = [1]
line = [1]
for i in range(10):
    for item in line:
        print(item, end=' ')
    print('')
    upper_length = len(upper)
    for j in range(1, upper_length):
        line[j] = upper[j] + upper[j - 1]
    line.append(1)

    upper = line[:]


################################################
if __name__ == '__main__':
    a = []
    for i in range(10):
        a.append([])
        for j in range(10):
            a[i].append(0)
    for i in range(10):
        a[i][0] = 1
        a[i][i] = 1
    for i in range(2,10):
        for j in range(1,i):
            a[i][j] = a[i - 1][j-1] + a[i - 1][j]
    from sys import stdout
    for i in range(10):
        for j in range(i + 1):
            stdout.write(str(a[i][j]))
            stdout.write(' ')
        print
