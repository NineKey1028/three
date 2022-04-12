# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 22:56:49 2022

@author: 105522236 陳柏昌
"""
#第一個作業
for i in range(1,10):
    for a in range(i):
        print(i,end='')
    print()
print()

#第二個作業
for i in range(9,1,-1):
    for a in range(i):
        print(i,end='')
    print()
print()

#第三個作業
for i in range(9,0,-2):
    for a in range(i):
        print(i,end='')
    print()
print()

#第四個作業
for i in range(1,100):
    if i % 2 !=0 or i ==2:
        if i % 3 !=0 or i ==3:
            if i % 5 !=0 or i ==5:
                if i % 7 !=0 or i == 7:
                    if i % 13 !=0 or i == 13:
                        print(i," ",end="")


