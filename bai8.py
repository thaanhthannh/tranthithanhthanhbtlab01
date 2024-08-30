# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:47:28 2024

@author: Thanh Thanh
"""
print("Cong thuc BMI = Can_nang (kg)/Chieu_cao**2 (m)")
can_nang=float(input("Nhap can nang cua ban (kg):"))
chieu_cao_cm=float(input("Nhap chieu cao cua ban (cm):"))
chieu_cao_m=chieu_cao_cm/100
BMI=can_nang/chieu_cao_m**2
print("Ket qua BMI cua ban:", round(BMI,2))
if BMI<18.5: 
    print("Ban thieu can")
if 18.5<=BMI<=24.9: 
    print("Ban binh thuong")
if 25<=BMI<=29.9: 
    print("Ban thua can")
if BMI>29.9: 
    print("Ban beo phi")