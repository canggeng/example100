#! /bin/bash

__author__ = 'zzj'
'''
题目：求100之内的素数。
'''

print("2是素数")
print("3是素数")
print("5是素数")
for i in range(4, 100):
    for j in range(2, i // 2):
        if i % j == 0:
            break

        if j == (i // 2 - 1):
            print(f"{i}是素数")


###################################
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))

for num in range(lower, upper + 1):
    # 素数大于 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)