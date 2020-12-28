#! /bin/bash
__author__ = 'zzj'
'''
题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天
'''


def leap_year(year):
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        return True
    else:
        return False


months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


total_days = 0
date = input("请输入年月日，举例：2000-1-15\n")

try:
    year, month, day = date.split('-')

    year = int(year)
    month = int(month if 0 < int(month) <= 12 else print("月份输入错误"))
    day = int(day if 0 < int(day) <= 31 else print("日期输入错误"))
    if month == 2 and day > 29:
        raise Exception("请输入正确年月日")
except Exception:
    print("请正确输入年月日")

if month > 1:
    for i in range(0, month - 1):
        total_days += days[i]
    if leap_year(year) and month > 2:
        total_days += 1

total_days += day

print(f"{date}是全年的第{total_days}天")


##############################################################################

# !/usr/bin/python3

year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day:\n'))

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print('data error')
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print('it is the %dth day.' % sum)