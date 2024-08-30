# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 22:35:10 2024

@author: Thanh Thanh
"""
#Bai21
n=int(input("Nhap so bat ky:"))
chuso={
       0:"Khong",
       1:"Mot",
       2:"Hai",
       3:"Ba",
       4:"Bon",
       5:"Nam",
       6:"Sau",
       7:"Bay",
       8:"Tam",
       9:"Chin"
       }
if 0<=n<=9:
    print("Chu so tuong ung la:", chuso[n])
else:
    print("Khong doc duoc")