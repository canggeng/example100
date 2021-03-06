#! /bin/bash

__author__ = 'zzj'
'''
题目：求0—7所能组成的奇数个数。
'''
digit = 1
total = 0
num = 0
long = 8
for i in range(long):
    if i % 2 == 1:
        num += 1
while digit <= long:
    if digit == 1:
        print(num)
        total += num
        digit += 1
        continue

    tmp = long ** (digit - 2)
    print(num * (long - 1) *tmp)
    total += num * (long - 1) *tmp
    digit += 1

print(total)


#######################################
if __name__ == '__main__':
    sum = 4
    s = 4
    for j in range(2,9):
        print(sum)
        if j <= 2:
            s *= 7
        else:
            s *= 8
        sum += s
    print('sum = %d' % sum)