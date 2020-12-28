#! /bin/bash
__author__ = 'zzj'
'''
题目：输入某年某月某日，判断这一天是这一年的第几天？
'''


def leap_year(year):
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        return True
    else:
        return False


months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
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
        continue

    if month > 1:
        for i in range(0, month - 1):
            total_days += days[i]
        if leap_year(year) and month > 2:
            total_days += 1

    total_days += day

    print(f"{date}是全年的第{total_days}天")
