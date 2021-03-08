#! /bin/bash

__author__ = 'zzj'
'''
题目：从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。
'''
a = input("请输入字符，以#结束： ")
with open("e:\\tmp.txt", 'a') as f:
    while True:
        for s in a:
            if s != '#':
                f.write(s)
            else:
                break
        if s != '#':
            a = input("请输入字符，以#结束： ")
        else:
            break


####################################################
if __name__ == '__main__':
    from sys import stdout
    filename = input('输入文件名:\n')
    fp = open(filename,"w")
    ch = input('输入字符串:\n')
    while ch != '#':
        fp.write(ch)
        stdout.write(ch)
        ch = input('')
    fp.close()