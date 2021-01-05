#! /bin/bash
__author__ = 'zzj'

'''
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
'''
score = int(input("请输入成绩: "))
if score >= 90:
    print("成绩为A")
elif 60 <= score <= 89:
    print("成绩为B")
else:
    print("成绩为C`")
