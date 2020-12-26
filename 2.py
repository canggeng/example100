#! /bin/bash
__author__ = 'zzj'
while True:
    i = int(input("请输入利润："))

    arr = [100000, 200000, 400000, 600000, 1000000]
    rat = [0.1, 0.075,  0.05,   0.03,   0.015,  0.01]
    r = 0
    for a in range(0, len(arr)):
        if i <= arr[a]:
            i -= arr[a-1]
            r += i * rat[a]
            print(r)
            break
        else:
            d = arr[a] - arr[a-1] if a > 0 else arr[a]
            r += d * rat[a]
            print(r)

    # r10 = 100000 * 0.1
    # r20 = 100000 * 0.075
    # r40 = 200000 * 0.05
    # r60 = 200000 * 0.03
    # r100 = 400000 * 0.015
    #
    # if i <= 100000:
    #     r = i * 0.1
    # elif i <= 200000:
    #     r = r10 + (i - 100000) * 0.075
    # elif i <= 400000:
    #     r = r10 + r20 + (i - 200000) * 0.05
    # elif i <= 600000:
    #     r = r10 + r20 + r40 + (i - 400000) * 0.03
    # elif i <= 1000000:
    #     r = r10 + r20 + r40 + r60 + (i - 600000) * 0.015
    # else:
    #     r = r10 + r20 + r40 + r60 + r100 + (1 - 1000000) * 0.01

    print(f"获得的奖金为：{r}")
    # i = int(input('净利润:'))
    # arr = [1000000, 600000, 400000, 200000, 100000, 0]
    # rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    # r = 0
    # for idx in range(0, 6):
    #     if i > arr[idx]:
    #         r += (i - arr[idx]) * rat[idx]
    #         print((i - arr[idx]) * rat[idx])
    #         i = arr[idx]
    # print(r)
