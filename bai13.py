# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:57:04 2024

@author: Thanh Thanh
"""
#Bai13
ngay=input("Nhap ngay:")
thang=input("Nhap thang:")
nam=input("Nhap nam:")
print("a) {0}/{1}/{2}".format(ngay,thang,nam))
print("b) {0}/{1}/{2}".format(ngay,thang,nam[2:]))
print("c) {0}/{1}/{2}".format(nam,thang,ngay))
#Lam nguoc lai
print("Lam nguoc lai:")
print("a) {0}/{1}/{2}".format(nam,thang,ngay))
print("b) {0}/{1}/{2}".format(nam[2:],thang,ngay))
print("c) {0}/{1}/{2}".format(ngay,thang,nam))




