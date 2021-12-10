# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 21:17:30 2021

@author: controller
"""

import numpy as np
import matplotlib.pyplot as plt
def CoD(x, y, y_func):
    TSS = sum([(y[i] - np.mean(y))**2 for i in range(len(y))])
    RSS = sum([(y[i]-y_func[i])**2 for i in range(len(y))])
    R_2 = 1 - RSS/TSS
    return round(R_2,5)
#Standard
bp = (102.58+102.64+102.65+102.66)/4
std_read_pressure = [-396.1,-357.6,-320.0,-279.6,-237.5,-197.6,-161.1,-120.5,-79.6,-37.5,0.2]
std_read_mmHg = np.array([40.00,36.15,32.25,28.25,24.05,20.0,16.3,12.2,8.15,3.9,0.15]) 
std_read_mmHg = std_read_mmHg*10
std_mmHg = bp*7.5 - std_read_mmHg
std = np.polyfit(std_read_pressure, std_mmHg,1)
fig1,ax1 = plt.subplots(figsize=(10,7))
ax1.scatter(std_read_pressure, std_mmHg,s=15,label="raw data")
x = np.arange(-410,15,0.02)
ax1.plot(x,np.poly1d(std)(x),c="black",label="fitting curve\ny={}x+{}".format(round(std[0],3),round(std[1],3)))
ax1.set_xlabel("Reading pressure")
ax1.set_ylabel("Actual pressure(mmHg)")
ax1.legend()
#Experience
read_pressure = [0,-34.0,-74.0,-115.1,-156.8,-196.1,
                 -236.4,-277.3,-316.3,-356.1,-395.8,-397.1,-356.5,-316.3,-276.5,
                 -237.5,-196.7,-156.3,-115.6,-74.6,-35.5,0.2,-34.2,
                 -75.9,-114.9,-156.7,-197.7,-235.7,-276.2,-317.6,-357.1,-396.3]
temp = np.array([(80.898+80.893+80.895)/3,79.360,77.531,75.535,73.403,71.278,
                 68.997,66.530,64.010,61.266,58.300,58.202,61.240,64.024,66.626,
                 68.935,71.274,73.437,75.519,77.503,79.334,81.005,79.396,
                 77.473,75.565,73.431,71.231,69.072,66.762,63.968,61.242,58.278])
#delete the point:(0.2, 79.949) 
kPa = np.poly1d(std)(read_pressure)
lnp = np.log(kPa)
T = 1/(temp+273.15)
fit = np.polyfit(lnp,T,1)
R = CoD(lnp,T,np.poly1d(fit)(lnp))
Tnor = 1/np.poly1d(fit)(np.log(760))
fig2,ax2 = plt.subplots(figsize=(10,7))
ax2.scatter(lnp,T,s=15,label="raw_data")
x=np.arange(5.8,6.67,0.001)
ax2.plot(x,np.poly1d(fit)(x),c="black",label="fitting curve\ny={}x+{}\nCoD={}".format(round(fit[0],6),round(fit[1],6),R))
ax2.set_xlabel("ln(p)")
ax2.set_ylabel("1/T")
ax2.legend()

fig3,ax3=plt.subplots(figsize=(10,7))
x=np.arange(350,800,0.01)
ax3.scatter(kPa,temp+273.15,s=15,label="raw data")
ax3.plot(x,1/np.poly1d(fit)(np.log(x)),c="black",label="fitting curve")
ax3.scatter(760,Tnor,s=75,c="red",label="Normal boil point")
ax3.set_ylim(325,360)
ax3.plot([760,760],[325,Tnor],"--",c="red")
ax3.set_xlim(340,810)
ax3.plot([340,760],[Tnor,Tnor],"--",c="red")
ax3.set_yticks(list(range(325,365,5))+[Tnor])
ax3.set_xticks([400,500,600,700,760,800])
ax3.set_xlabel("Pressure(mmHg)")
ax3.set_ylabel("T(K)")
ax3.legend()

fit2 = np.polyfit(T,lnp,1)
R2 = CoD(T,lnp,np.poly1d(fit2)(T))
fig4,ax4 = plt.subplots(figsize=(10,7))
ax4.scatter(T,lnp,s=15,label="raw_data")
x=np.arange(0.00280,0.00305,0.00001)
ax4.plot(x,np.poly1d(fit2)(x),c="black",label="fitting curve\ny={}x+{}\nCoD={}".format(round(fit2[0],2),round(fit2[1],2),R2))
ax4.set_xlabel("1/T,T(K)")
ax4.set_ylabel("ln(p),p(mmHg)")
ax4.legend()
