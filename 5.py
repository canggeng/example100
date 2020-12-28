#! /bin/bash
__author__ = 'zzj'

'''
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，
然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
'''

x = input("请输入x的值：")
y = input("请输入y的值：")
z = input("请输入z的值：")

if x > y:
    tmp = x
    x = y
    y = tmp
if x > z:
    tmp = x
    x = z
    z = tmp
if y > z:
    tmp = y
    y = z
    z = tmp

print(f"从小到大的三个数字为：{x}、{y}、{z}")


################################################################################################
# !/usr/bin/python3

l = []
for i in range(3):
    x = int(input('integer:\n'))
    l.append(x)
l.sort()
print(l)
