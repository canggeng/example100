#! /bin/bash
__author__ = 'zzj'
'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
'''

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
blank = ' '
numbers = '1234567890'

a = input("请输入一行字符：")

l = len(a)

chars_num = 0
blank_num = 0
numbers_num = 0
others_num = 0

for c in a:
    if c in chars:
        chars_num += 1
    elif c in blank:
        blank_num += 1
    elif c in numbers:
        numbers_num += 1
    else:
        others_num += 1

print(f"字母数为：{chars_num}")
print(f"空格数为：{blank_num}")
print(f"数字数为：{numbers_num}")
print(f"其他字符数为：{others_num}")


######################################
s = input('请输入一个字符串:\n')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print ('char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others))