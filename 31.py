#! /bin/bash

__author__ = 'zzj'
'''
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
'''
weekdays = ['Monday', 'Tuesday', 'Thursday', 'Wednesday', 'Friday', 'Saturday', 'Sunday']

chars = input("查询周几的英文怎么写：")
chars = chars.lower()
if chars.startswith('m'):
    print(weekdays[0])
elif chars.startswith('tu'):
    print(weekdays[1])
elif chars.startswith('th'):
    print(weekdays[2])
elif chars.startswith('w'):
    print(weekdays[3])
elif chars.startswith('f'):
    print(weekdays[4])
elif chars.startswith('sa'):
    print(weekdays[5])
elif chars.startswith('su'):
    print(weekdays[6])
else:
    print('请输入正确的日期开头字母')


############################################
letter = input("please input:")
# while letter  != 'Y':
if letter == 'S':
    print('please input second letter:')
    letter = input("please input:")
    if letter == 'a':
        print('Saturday')
    elif letter == 'u':
        print('Sunday')
    else:
        print('data error')

elif letter == 'F':
    print('Friday')

elif letter == 'M':
    print('Monday')

elif letter == 'T':
    print('please input second letter')
    letter = input("please input:")

    if letter == 'u':
        print('Tuesday')
    elif letter == 'h':
        print('Thursday')
    else:
        print('data error')

elif letter == 'W':
    print('Wednesday')
else:
    print('data error')