#! /bin/bash

__author__ = 'zzj'
'''
题目：利用ellipse 和 rectangle 画图。
'''

from tkinter import *

canvas = Canvas(width=900, height=1200, bg='white')

x0 = 50
y0 = 50
c0 = 2
x1 = 55
y1 = 55
c1 = 20

x = 600
y = 600
w0 = 100
h0 = 40
w1 = 20
h1 = 100
c = 10
for i in range(15):
    canvas.create_rectangle(x0, y0, x1, y1)
    x0 -= c0
    y0 -= c0
    x1 += c1
    y1 += c1

    canvas.create_oval(x-w0, y-h0, x+w0, y+h0)
    w0 += c
    h0 += c

    canvas.create_oval(x - w1, y - h1, x + w1, y + h1)
    h1 += c


canvas.pack()
mainloop()


######################################################
if __name__ == '__main__':
    canvas = Canvas(width = 400,height = 600,bg = 'white')
    left = 20
    right = 50
    top = 50
    num = 15
    for i in range(num):
        canvas.create_oval(250 - right,250 - left,250 + right,250 + left)
        canvas.create_oval(250 - 20,250 - top,250 + 20,250 + top)
        canvas.create_rectangle(20 - 2 * i,20 - 2 * i,10 * (i + 2),10 * ( i + 2))
        right += 5
        left += 5
        top += 10

    canvas.pack()
    mainloop()