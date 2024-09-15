# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 09:55:21 2024

@author: Student
"""


n = int(input("Nhập một số nguyên dương: "))

giai_thua = 1

for i in range(1, n + 1):
    giai_thua *= i
print(f"Giai thừa của {n} là: {giai_thua}")
