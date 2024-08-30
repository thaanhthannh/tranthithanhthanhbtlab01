# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 23:33:03 2024

@author: Thanh Thanh
"""
#Bai22
a=int(input("Nhap he so a:"))
b=int(input("Nhap he so b:"))
print("Phuong trinh bac nhat co dang: {0}X + {1} = 0".format(a,b))
#giai phuong trinh
if a==0:
    if b==0:
        print("Phuong trinh vo so nghiem")
    else:
        print("Phuong trinh vo nghiem")
else:
    print("Phuong trinh co nghiem phan biet:",-b/a)