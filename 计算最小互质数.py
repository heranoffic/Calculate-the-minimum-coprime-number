# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 14:24:34 2022

@author: Administrator
"""

#b=a=int(input("a="))
def fct1(a):
 for i in range(2,a):
     b=a
     d=i
     while i!=b:
         if b>i:
             b -=i
         else:
             i -=b
     if i==b:
         if i==1:
             c=d
             return c
             break     
