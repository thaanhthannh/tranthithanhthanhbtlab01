# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 10:19:13 2024

@author: Thanh Thanh
"""
#Bai27
#Tinh chu vi, dien tich hinh hoc
#Nhap du lieu
hinh=input("Nhap hinh muon tinh:")
v="hinh_vuong"
n="hinh_chu_nhat"
t="hinh_tron"
#Tinh chu vi, dien tich cac hinh
if hinh=="v":
    canh=int(input("Nhap canh hinh vuong:"))
    print("Chu vi hinh vuong:", canh*4) #canhx4
    print("Dien tich hinh vuong:", canh**2) #canh^2
elif hinh=="n":
    rong=(int(input("Nhap chieu rong:")))
    dai=(int(input("Nhap chieu dai:")))
    print("Chu vi hinh chu nhat:", (dai+rong)*2) #2x(dai+rong)
    print("Dien tich hinh chu nhat:", dai*rong) #daixrong
elif hinh=="t":
    r=int(input("Nhap ban kinh hinh tron:"))
    import math
    print("Chu vi hinh tron:", round(2*math.pi*r,2)) #2xpixr
    print("Dien tich hinh tron:", round(math.pi*(r)**2,2)) #pixr^2
else:
     print("Khong xac dinh")