#! /bin/bash

__author__ = 'zzj'
'''
题目：两个变量值互换。
'''
a = 4324
b = 'dingvew'
print("before exchange")
print(f"a={a}")
print(f"b={b}")

a, b = b, a
print("after exchange")
print(f"a={a}")
print(f"b={b}")


##########################################
def exchange(a, b):
    a, b = b, a
    return (a, b)


if __name__ == '__main__':
    x = 10
    y = 20
    print('x = %d,y = %d' % (x, y))
    x, y = exchange(x, y)
    print('x = %d,y = %d' % (x, y))
