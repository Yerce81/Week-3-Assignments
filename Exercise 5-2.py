# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 15:36:14 2022

@author: jg198
"""

a = int(input("Choose a number for a: "))
b = int(input("Choose a number for b: "))
c = int(input("Choose a number for c: "))
n = int(input("Choose a number for n: "))

def check_fermat(n):
    if n > 2:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work.")
check_fermat(n)