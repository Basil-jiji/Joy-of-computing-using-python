# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 16:19:37 2022

@author: basil
"""
import random

def evolve(x):
    indx = random.randint(0,len(x)-1)
    p = random.randint(1,100)
    print(p)
    if(p==1):
        if(x[indx] =='0'):
            x[indx] = '1'
        else:
            x[indx]='0'

with open("DNA.txt") as myfile:
    x = myfile.read()
    x=list(x) #Converting to list
for i in range(0,10000):
    evolve(x)
print(x)