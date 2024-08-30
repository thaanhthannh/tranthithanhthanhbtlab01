# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 23:54:07 2024

@author: Thanh Thanh
"""
#Bai23
#giai phuong trinh bac 2
a=int(input("Nhap he so a:"))
b=int(input("Nhap he so b:"))
c=int(input("Nhap he so c:"))
print("Phuong trinh bac 2 co dang: {0}X^2 + {1}X + {2} = 0".format(a,b,c))     
import math
delta=b**2 - 4*a*c
if delta<0:
    print("Phuong trinh vo nghiem")
elif delta==0:
    print("Phuong trinh co nghiem kep:", -b/(2*a))
else:
    print("Phuong trinh co 2 nghiem phan biet:")
    x1=(-b-math.sqrt(delta))/(2*a)
    print("x1={0}".format(x1))
    x2=(-b+math.sqrt(delta))/(2*a)
    print("x2={0}".format(x2))