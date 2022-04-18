# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 21:25:57 2022

@author: NineKey1028
"""

#4 有一個分數序列 ： 2/1,3/2,5/3,8/5 , 13/8 , 21/13 ..求這個數列的前20項和
h = []  
     

p = 2
r = 1
c = r
for i in range(20):
    print(p,"/",c,sep="",end=",")
    h.append(p)
    h.append(c)
    c = p
    p += r
    r = c
print()
print("數值總和為:",sum(h))