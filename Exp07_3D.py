# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 12:47:05 2021

@author: controller
"""

import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

S = np.r_[np.ones(6)*5,np.ones(4)*10]
H = np.array([2,2,2,2,4,4,2,2,4,4])
s = ['v','^','o','^','v','o','v','o','v','o']
color = []
T = []
for i in s:
    if i == 'v':
        T.append("30")
        color.append("b")
    elif i == 'o':
        T.append("35")
        color.append('orange')
    else:
        T.append("40")
        color.append("r")

def axset(fig,z,zfit,zname):
    maxz = max(z)*(1+zfit)
    minz = min(z)*(1-zfit*5)
    sep_point = np.linspace(minz,maxz,4)[1:-1]
    sc = ['b','r']
    ax = fig.add_subplot(111,projection="3d")
    ax.set_xlabel("Relative concentration of Sucrose")
    ax.set_ylabel('Relative concentration of HCl')
    ax.set_zlabel(zname)
    ax.set_xlim(0,15)
    ax.set_ylim(0,6)
    ax.set_zlim(minz,maxz)
    ax.set_xticks([0,5,10,15])        
    ax.set_yticks([0,2,4,6])
    x = np.linspace(0, 15, 15)
    y = np.linspace(0, 6, 6)
    X, Y = np.meshgrid(x, y)
    for i in range(len(sep_point)):
        ax.plot_surface(X,Y,Z=X*0+sep_point[i],alpha=0.1,color=sc[i]) 
    ax.plot([5,5],[2,2],[minz,maxz],"--",c="g",label="Fixed concentration lines")
    for k in range(len(sep_point)):
        ax.scatter([5]*2,[2]*2,sep_point[k],c=sc[k],s=15,alpha=0.3,label="{}={:.3e}".format(zname,sep_point[k]))
    for (i,j) in [(1,2),(2,1),(2,2)]:
        ax.plot([5*i,5*i],[2*j,2*j],[minz,maxz],"--",c="g")
        for k in range(len(sep_point)):
            ax.scatter([5*i]*2,[2*j]*2,sep_point[k],c=sc[k],s=15,alpha=0.3)    
#    for i in range(len(sep_point)):
#        z = [sep_point[i],sep_point[i]]
#        ax.plot([0,15],[2,2],z,"--",c=sc[i],alpha=0.3)
#        ax.plot([0,15],[4,4],z,"--",c=sc[i],alpha=0.3)
#        ax.plot([5,5],[0,6],z,"--",c=sc[i],alpha=0.3)
#        ax.plot([10,10],[0,6],z,"--",c=sc[i],alpha=0.3)
    return ax

k = [4.200E-04,1.610E-03,8.295E-04,1.610E-03,1.296E-03,2.537E-03,4.245E-04,8.483E-04,1.330E-03,2.626E-03]
fig = plt.figure(figsize=(9,9))
ax = axset(fig,k,0.05,"k(/s)")
for i in range(10):
    if i in [0,2,3]:
        ax.scatter(S[i],H[i],k[i],c=color[i],marker=s[i],s=70,label="T={}°C".format(T[i]))
    else:
        ax.scatter(S[i],H[i],k[i],c=color[i],marker=s[i],s=70)
ax.legend()

#E
S1 = [5,5,5,10,10]
H1 = np.array([2,2,4,2,4])
s1 = ['o','^','v','v','v']
color1 = []
T1 = [35,37.5,32.5,32.5,32.5]
for i in s1:
    if i == 'v':
        color1.append("b")
    elif i == 'o':
        color1.append('orange')
    else:
        color1.append("r")
 
E = [106.1,106.4,104.3,107.5,105.7]
fig = plt.figure(figsize=(9,9))
ax = axset(fig,E,0.001,"Ea(kJ/mol)")
for i in range(5):
    if i in [0,1,2]:
        ax.scatter(S1[i],H1[i],E[i],c=color1[i],marker=s1[i],s=70,label="T={}°C".format(T1[i-1]))
    else:
        ax.scatter(S1[i],H1[i],E[i],c=color1[i],marker=s1[i],s=70)
ax.legend()
