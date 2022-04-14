# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 20:33:39 2022

@author: NineKey1028
"""

import random
a = int(input("請輸入最小值："))
b = int(input("請輸入最大值："))
ans = random.randint(a,b)
c = 0
d = 0

while c != ans :
    print("範圍:{}~{}".format(a,b))
    c = int(input("請輸入答案："))
    
    if d == 5:
        print("偷偷告訴你答案是{}".format(ans))
    if c <= a or c >= b:
        print("輸入錯誤，請重新輸入")
        continue
    if c > ans:
        d += 1
        print("已猜了{}次".format(d))
        b = c
    if c < ans:
        d += 1
        print("已猜了{}次".format(d))
        a = c
print("-"*20)
d += 1
print("答對了，答案是{}".format(ans))
print("共猜了{}次".format(d))
input("請按任意鍵結束")

