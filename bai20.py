# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 22:19:10 2024

@author: Thanh Thanh
"""
#Bai20
a=int(input("Nhap so nguyen thu 1:"))
b=int(input("Nhap so nguyen thu 2:"))
c=int(input("Nhap so nguyen thu 3:"))
#gia su a la so lon nhat
solon1=a
if b>solon1:
    solon1=b
if c>solon1:
    solon1=c
print("So co gia tri lon nhat la:", solon1)
