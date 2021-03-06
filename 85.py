#! /bin/bash

__author__ = 'zzj'
'''
题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
'''


def num9(digit):
    result = 0
    for j in range(digit):
        result += 9 * (10 ** j)

    return result


odd = int(input("请输入一个奇数： "))

if odd % 2 == 0:
    print("输入的为偶数")
    exit(0)

i = 1
while True:
    n = num9(i)
    if n % odd == 0:
        print(f"{odd}能整除{i}个9\n结果为：{n}/{odd}={n / odd}")
        break
    i += 1

##############################
if __name__ == '__main__':
    zi = int(input('输入一个数字:\n'))
    n1 = 1
    c9 = 1
    m9 = 9
    sum = 9
    while n1 != 0:
        if sum % zi == 0:
            n1 = 0
        else:
            m9 *= 10
            sum += m9
            c9 += 1
    print('%d 个 9 可以被 %d 整除 : %d' % (c9, zi, sum))
    r = sum / zi
    print('%d / %d = %d' % (sum, zi, r))
