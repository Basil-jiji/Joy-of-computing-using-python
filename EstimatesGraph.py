# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 13:52:55 2022

@author: basil
"""

import matplotlib.pyplot as plt
import statistics
Estimates =[1182, 1329, 1179, 565, 1478, 762, 630, 829, 860, 1311, 757, 298, 556, 1458, 516, 693, 896, 1189, 765, 384, 1171, 1092, 222, 711, 1225, 871, 363, 662, 1396, 578, 80, 273, 972, 218, 437, 1187, 1342, 557, 1173, 291, 112, 791, 151, 962, 1310, 179, 631, 742, 1255, 611, 1289, 1217, 969, 864, 699, 1130, 562, 550, 1031, 839, 540, 1005, 888, 484, 728, 966, 74, 309, 19, 961, 1412, 1489, 287, 212, 576 ]
y=[]

Estimates.sort()
trimV=int(0.1*(len(Estimates)))
Estimates = Estimates[trimV:]
Estimates = Estimates[:len(Estimates)-trimV]
for i in range(len(Estimates)):
    y.append(5)
plt.plot(Estimates, y,'r--')
plt.plot([statistics.mean(Estimates)],[5],'ro')
plt.plot([statistics.median(Estimates)],[5],'bs')
plt.plot([900],[5],'g^')