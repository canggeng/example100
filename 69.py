#! /bin/bash

__author__ = 'zzj'
'''
题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
'''


def pop3(pop_list):
    count = 1
    index = 0
    while True:
        if count % 3 == 0:
            pop_list.pop(index)
            if len(pop_list) == 1:
                break
        else:
            index += 1
        count += 1
        if index == len(pop_list):
            index = 0

    return pop_list[0]


n = int(input("有n个人围成一圈，请输入n: "))
pop_list = []
for i in range(1, n + 1):
    pop_list.append(i)

last = pop3(pop_list)

print(f"从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，最后留下的是原来第{last}号的那位")


############################################
if __name__ == '__main__':
    nmax = 50
    n = int(input('请输入总人数:'))
    num = []
    for i in range(n):
        num.append(i + 1)

    i = 0
    k = 0
    m = 0

    while m < n - 1:
        if num[i] != 0: k += 1
        if k == 3:
            num[i] = 0
            k = 0
            m += 1
        i += 1
        if i == n: i = 0

    i = 0
    while num[i] == 0: i += 1
    print(num[i])