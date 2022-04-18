# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 21:28:42 2022

@author: NineKey1028
"""
k = True
while k:
    i = int(input("請輸入一個大於0的整數："))
    if i <= 0 :
        print()
        print("輸入資料錯誤!!")
    else:
        k =False
x = i
c = False
b = 0
print("-"*50)
print("因 式 分 解：")
print(i,"= ",end="")
while i != 1:

    for l in range(2,i+1):
        if c and i % l ==0:
            print(" X ",end="")
        if i % l ==0:            
            print(l,end="")
            b += 1
            i /= l
            i = int(i)
            c = True         
            break
if x == 1:
    print("1 X 1",end="")
if b == 1:    
    print(" X",1)
    print(x,"是質數")


        
