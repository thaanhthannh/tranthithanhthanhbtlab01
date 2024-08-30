# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 20:46:55 2024

@author: Thanh Thanh
"""
#Bai19
a=int(input("Nhap so nguyen thu 1:"))
b=int(input("Nhap so nguyen thu 2:"))
c=int(input("Nhap so nguyen thu 3:"))
d=int(input("Nhap so nguyen thu 4:"))
#gia su a la nho nhat
sonho1=a
if b<sonho1:
    sonho1=b
if c<sonho1:
    sonho1=c
if d<sonho1:
    sonho1=d
print("So co gia tri nho nhat:", sonho1)

