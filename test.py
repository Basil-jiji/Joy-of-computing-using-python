# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 10:14:14 2022

@author: basil
"""

n,m = map(int,input().split())

l=[int(i) for i in input().split()]

sum=0

for i in l:
  sum+=i
  
s=sum//m

ans = sum-(s*m)

print(ans,end="")