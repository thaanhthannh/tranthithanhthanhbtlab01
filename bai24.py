# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 09:03:50 2024

@author: Thanh Thanh
"""
#Bai24
gio=int(input("Nhap vao gio:"))
phut=int(input("Nhap vao phut:"))
giay=int(input("Nhap vao giay:"))
if 0<=gio<=24 and 0<=phut<=60 and 0<=giay<=60:
    print("{0} gio {1} phut {2} giay do hop le".format(gio,phut,giay))
else:
    print("{0} gio {1} phut {2} giay do khong hop le".format(gio,phut,giay))