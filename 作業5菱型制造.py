# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 22:04:51 2022

@author: NineKey1028
"""
c = 1
m = "*"
for i in range(4):
    print("{:^7}".format(m*c))
    c +=2
c-=4
for x in range(3,0,-1):
    
    print("{:^7}".format(m*c))
    c -=2