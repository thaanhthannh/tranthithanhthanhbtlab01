# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 19:45:10 2024

@author: Thanh Thanh
"""
#Bai15
print("Bieu thuc:","\n""((a+b)/(a**1/3 + b**1/3)-((a*b)**1/3)):((a**1/3 - b**1/3)**2)")
a=float(input("Nhap so thu 1:"))
b=float(input("Nhap so thu 2:"))
x=(a+b)/(a**(1/3) + b**(1/3))
y=(a*b)**(1/3)
z=(a**(1/3) - b**(1/3))**2
print("Ket qua la:", (x-y)/z)