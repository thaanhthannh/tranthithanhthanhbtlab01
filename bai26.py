# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 09:55:09 2024

@author: Thanh Thanh
"""
#bai26a
#In ra man hinh cac so theo thu tu tang dan
#Nhap du lieu
a=int(input("Nhap so thu 1:"))
b=int(input("Nhap so thu 2:"))
c=int(input("Nhap so thu 3:"))
#In so tang dan
if a>b:
    a,b=b,a
if a>c:
    a,c=c,a
if b>c:
    b,c=c,b
print("Thu tu tang dan cua ba so la:", a,b,c)
#bai26b
#Nhap du lieu
a=int(input("Nhap so thu 1:"))
b=int(input("Nhap so thu 2:"))
c=int(input("Nhap so thu 3:"))
d=int(input("Nhap so thu 4:"))
if a>b:
    a,b=b,a
if a>c:
    a,c=c,a
if b>c:
    b,c=c,b
if c>d:
    c,d=d,c
print("Thu tu tang dan cua bon so la:", a,b,c,d)