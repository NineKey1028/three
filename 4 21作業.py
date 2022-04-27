# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 20:38:20 2022

@author: NineKey1028
"""

import json
import requests

url = "https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/json?page=0&size=1000"

data = requests.get(url)
bike = data.text
content = json.loads(bike)
h = []
for c in content:
    if h.count(c.get('sarea')) == 0:
        h.append(c.get('sarea'))
print("目前新北市有: ")
a = False
for k in h:
    if a:
        print("、",end= "")
    print(k,end="")
    a = True

x = input("請輸入要尋詢的區域: ")
for row in content:
    if row['sarea'] == x:
        print("地區",row['sarea'])
        print("站名",row['sna'])
        print("總數量",row['tot'])
        print("可借",row['sbi'])
        print("可停",row['bemp'])