# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 20:08:35 2024

@author: Thanh Thanh
"""
#Bai18
#thoigian1
gio1=int(input("Nhap gio thu 1:"))
phut1=int(input("Nhap phut thu 1:"))
giay1=int(input("Nhap giay thu 1:"))
#thoigian2
gio2=int(input("Nhap gio thu 2:"))
phut2=int(input("Nhap phut thu 2:"))
giay2=int(input("Nhap giay thu 2:"))
#Gep thoigian = giay phut gio
from datetime import timedelta
thoigian1=timedelta(hours=gio1,minutes=phut1,seconds=giay1)
thoigian2=timedelta(hours=gio2,minutes=phut2,seconds=giay2)
#tong 2 thoi gian
print("Tong 2 thoi gian =", thoigian1+thoigian2)
#hieu 2 thoi gian
print("Hieu 2 thoi gian =", abs(thoigian1-thoigian2))