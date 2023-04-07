# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 15:55:22 2022

@author: basil
"""

with open("file1.txt","r+") as myfile:
    print(myfile.read())    #Reading a file
    myfile.write("Iam fine")
myfile.close()
    