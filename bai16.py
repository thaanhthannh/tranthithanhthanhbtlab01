# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 19:53:29 2024

@author: Thanh Thanh
"""
#Bai16
gio=int(input("Nhap gio:"))
phut=int(input("Nhap phut:"))
giay=int(input("Nhap giay:"))
print("Gio da nhap: {0}h{1}p{2}s".format(gio,phut,giay))
print("Tong so giay la: {0} giay".format(gio*3600+phut*60+giay))