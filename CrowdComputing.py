# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 12:15:07 2022

@author: basil
"""

from statistics import mean
from scipy import stats

Estimates =[1182, 1329, 1179, 565, 1478, 762, 630, 829, 860, 1311, 757, 298, 556, 1458, 516, 693, 896, 1189, 765, 384, 1171, 1092, 222, 711, 1225, 871, 363, 662, 1396, 578, 80, 273, 972, 218, 437, 1187, 1342, 557, 1173, 291, 112, 791, 151, 962, 1310, 179, 631, 742, 1255, 611, 1289, 1217, 969, 864, 699, 1130, 562, 550, 1031, 839, 540, 1005, 888, 484, 728, 966, 74, 309, 19, 961, 1412, 1489, 287, 212, 576 ]
Estimates.sort()

m = stats.trim_mean(Estimates,0.1)
print(m)

#for i in range(len(Estimates)):
#   print(Estimates[i])
    
#trimV = int(0.1*len(Estimates))
#Estimates = Estimates[trimV:]
#Estimates = Estimates[:len(Estimates) - trimV]
#print (mean(Estimates))
