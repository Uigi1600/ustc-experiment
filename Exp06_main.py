# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 22:41:04 2021

@author: controller
"""
import numpy as np
def CoD(x, y, y_func):
    TSS = sum([(y[i] - np.mean(y))**2 for i in range(len(y))])
    RSS = sum([(y[i]-y_func[i])**2 for i in range(len(y))])
    R_2 = 1 - RSS/TSS
    return round(R_2,5)

E0 = (435.977+435.320+436.190)/3
E00 = 0.4577
E0fix = E0/1000+8.314*(30+273.15)/(2*96485)*np.log(1/0.1)

T = np.array([30,35,40,45])
def E(t,E25,a,b):
    E = E25+a*(t-25)+0.5*b*pow(t-25,2)
    return E
from scipy import optimize as op
E1 = [(495.775+495.665+495.590)/3,
      (491.740+491.695+491.652)/3,
      (488.587+488.554+488.512)/3,
      (485.726+485.734+485.756)/3]
E1 = [i/1000 for i in E1]
def fun(x):
    return x*(x+0.1)-1.8E-10
a0 = 0.1
Cl = a0+op.fsolve(fun,0)
Ag = a0+op.fsolve(fun,0)
delta = 8.314*(T+273.15)/96485*np.log(1/(Cl*Ag))
E1 = E1 + delta
import matplotlib.pyplot as plt
fit = op.curve_fit(E,T,E1)[0]
def E(t):
    E25,a,b = fit[0],fit[1],fit[2]
    E = E25+a*(t-25)+0.5*b*pow(t-25,2)
    return E
X=np.arange(28,46,0.1)
plt.scatter(T,E1,label="raw data")
plt.plot(X,E(X),label="E(V)-t(°C)\nE={}+{}*(t-25)+{}*(t-25)^2\nCoD={}".format(
    round(fit[0],4),round(fit[1],4),round(fit[2],5)/2,CoD(T,E1,E(T))))
plt.xlabel("t(°C)")
plt.ylabel("E(V)")
plt.legend()
def dE(t):
    dE = fit[1]+fit[2]*(t-25)
    return dE

E10 = 0.5773#25C
E25 = fit[0]
Gm = -96485*E25 #T=25
Sm = 96485*dE(25)
Hm = Gm+(T[0]+273.15)*Sm
