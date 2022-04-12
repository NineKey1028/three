# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 17:13:22 2022

@author: NineKey1028
"""

a = float(input("第一個數字："))
b = float(input("第二個數字："))
c = input("算式")

if(c == "+"):
    print(a+b)
elif(c =="-"):
    print(a-b)
elif(c =="*"):
    print(a*b)
elif(c == "/"):
    print(a/b)
else:
    print("輸入錯誤")
