#! /bin/bash

__author__ = 'zzj'
'''
题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，
c说他不和x,z比，请编程序找出三队赛手的名单。
'''
jia = ['a', 'b', 'c']
yi = ['x', 'y', 'z']

a_index = jia.index('a')
c_index = jia.index('c')
count = 0
while True:
    if a_index == yi.index('x'):
        tmp = yi[(a_index + 1) % len(yi)]
        yi[(a_index + 1) % len(yi)] = 'x'
        yi[a_index] = tmp

    if c_index == yi.index('x'):
        tmp = yi[(c_index + 1) % len(yi)]
        yi[(c_index + 1) % len(yi)] = 'x'
        yi[c_index] = tmp

    if c_index == yi.index('z'):
        tmp = yi[(c_index + 1) % len(yi)]
        yi[(c_index + 1) % len(yi)] = 'z'
        yi[c_index] = tmp

    count += 1

    if a_index != yi.index('x') and c_index != yi.index('x') and c_index != yi.index('z'):
        break

print(jia)
print(yi)
print(count)

############################################################
for i in range(ord('x'),ord('z') + 1):
    for j in range(ord('x'),ord('z') + 1):
        if i != j:
            for k in range(ord('x'),ord('z') + 1):
                if (i != k) and (j != k):
                    if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                        print ('order is a -- %s\t b -- %s\tc--%s' % (chr(i),chr(j),chr(k)))