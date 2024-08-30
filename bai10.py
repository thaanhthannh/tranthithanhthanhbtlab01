# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:18:59 2024

@author: Thanh Thanh
"""
#Bai10
#Nhap bien so xe gom 4 so, dem nut
a=int(input("Nhap so thu 1:"))
b=int(input("Nhap so thu 2:"))
c=int(input("Nhap so thu 3:"))
d=int(input("Nhap so thu 4:"))
print("Bien so xe cua ban la: {0}{1}{2}{3}".format(a,b,c,d))
so_xe=a+b+c+d
nghin=so_xe//1000
tram=so_xe//100%10
chuc=so_xe//10%10
donvi=so_xe%10
e=nghin+tram+chuc+donvi
print("Bien so xe cua ban duoc {0} nut".format(e))