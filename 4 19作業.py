# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 23:36:38 2022

@author: NineKey1028
"""
'''
作業一
請用 for  來處理
data = [100,80,90,70,59,30,21,35]

請排序它，==> 從小到大 => [21,30,35,59,70,80,90,100]
請排序=> 從大到小  => [100,90,80,70,59,35,30,21]
'''
data = [100,80,90,70,59,30,21,35]
print("原值：",data)
print("-"*20)
a = []
for i in range(0,101,):
    c = 0
    c = data.count(i)
    while c >= 1:
        h = data.index(i)
        l = data.pop(h)
        a.append(l)  
        c = data.count(i)    
print("從小到大排序：",a)
print("-"*20)
data = [100,80,90,70,59,30,21,35]

a = []
for i in range(100,0,-1):
    c = 0
    c = data.count(i)
    while c >= 1:
        h = data.index(i)
        l = data.pop(h)
        a.append(l)  
        c = data.count(i)      
print("從大到小排序：",a)
print("-"*20)

'''
作業二
data =  [10,20,30,25,50,60]
請反轉內容
==> [60,50,25,30,20,10]
'''
data =  [10,20,30,25,50,60]
print("原值：",data)
a =[]
for i in range(6):
    b = data.pop()
    a.append(b)
print("反轉內容：",a)
'''
作業三。額外練習題
巴斯卡三角形 ，請用一簡串來處理
'''
print("{:^45}".format("巴斯卡三角形"))
n = 6
a =[]

for i in range(0,n):
    a.append([])
    a[i].append(1)
    for x in range(1,i):
        a[i].append(a[i-1][x-1]+a[i-1][x])
    a[i].append(1)
txt = ""
for k in range(n):
    for h in range(k):
        txt += str(a[k][h])+" "
    txt += "1"
    print("{:^50}".format(txt))
    txt = ""



