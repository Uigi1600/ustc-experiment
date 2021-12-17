# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 09:36:39 2021

@author: controller
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf
from scipy.optimize import fsolve
#Normalization curve
W1 = np.array([0.4911/5.0239,1.0044/5.0204,1.5096/5.0072,1.9977/5.0305,2.4937/4.9909,
         3.0064/5.0453,3.4912/5.0164,1-1.0076/4.9975,1-0.4974/5.0004,1])
mass = np.array([5.0239,5.0204,5.0072,5.0305,4.9909,
        5.0453,5.0164,4.9975,5.0004])
ri = np.array([1.3414,1.3503,1.3568,1.3621,1.36725,1.37155,1.37555,1.3791,1.3819,1.38305])
def d(W,a0,a1,a2,a3,a4,a5,a6):
    W = W*100
    a = [a0,a1,a2,a3,a4,a5,a6]
    for i in range(7):
        a[i] = a[i]*pow(W,i)
    return sum(a)
def ng(W,a0,a1,a2,a3,a4,a5,a6):
    p1 = W*(0.3829/0.8053)
    p2 = (1-W)*(0.33/1)
    ng = (p1+p2)*d(W,a0,a1,a2,a3,a4,a5,a6)+1
    return ng
X = np.arange(0,1,0.001)
fitn = cf(ng,W1,ri)[0]
def ng(W):
    p1 = W*(0.3829/0.8053)
    p2 = (1-W)*(0.33/1)
    ng = (p1+p2)*d(W,fitn[0],fitn[1],fitn[2],fitn[3],fitn[4],fitn[5],fitn[6])+1
    return ng
plt.plot(X,ng(X))
plt.xlabel("Mass fractiono of 1-propanol(%)")
plt.ylabel("Refraction index of mixture")
plt.legend(["RI - w1"])
plt.scatter(W1,ri)
#Exp：Li Yiran + Li Zongkai
P = 102.58
gas = [1.3830,1.3825,1.3807,1.3790,1.3779,1.3773,1.3766,1.3763,
          1.3347,1.3544,1.3662,1.37145,1.37335,
          1.3747,1.3754,1.37565]
gas = np.append(gas[8:],gas[:8][::-1])
liquid = [1.3831,1.3831,1.3830,1.3825,1.38155,1.3802,1.3778,1.3741,
          1.3326,1.33305,1.3338,1.3353,1.3382,
          1.34115,1.35465,1.3651]
liquid = np.append(liquid[8:],liquid[:8][::-1])
T_1 = np.array([97.526,95.652,93.093,90.754,89.179,
                88.442,88.051,88.063,
      100.219,98.327,96.683,94.547,92.238,
      89.065,88.186,88.347])
T_2 = np.array([97.527,95.651,93.095,90.758,89.177,88.441,
                88.050,88.062,
      100.218,98.197,96.661,94.513,92.203,
      89.105,88.187,88.345])
T_3 = np.array([97.525,95.658,93.098,90.755,89.171,88.448,88.051,88.063,
      100.219,98.412,96.731,94.598,92.223,
      89.008,88.191,88.345])
T = (T_1+T_2+T_3)/3
deltaT = (273.15+T)/(10)*(101.325-102.58)/101.325
T = T+deltaT
T = np.append(T[8:],T[:8][::-1])
Tl = np.append(T[:5],T[7:])
Tg = T
liq= np.append(liquid[:5],liquid[7:])
def ngtow(w,ng1):
    return (ng(w)-ng1)
vague = np.polyfit(ri,W1,6)
w1_ = np.array([fsolve(ngtow,np.poly1d(vague)(i),i)[0] for i in liquid])
w1 = np.array([fsolve(ngtow,np.poly1d(vague)(i),i)[0] for i in liq])
wg1 = np.array([fsolve(ngtow,np.poly1d(vague)(i),i)[0] for i in gas])
plt.scatter(w1_,T)
plt.scatter(wg1,T)
