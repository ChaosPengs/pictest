# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 10:28:14 2023

@author: Lenovo
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fs=18
w=0.4
lw=4
point_sz = 80
scale = [1,2,3,4,5,6,7]
bwith=2
#scale = [4,8,16,32,64,128,300] 152
#dc = [102, 68, 54, 39, 21, 12.3, 7.8]
#rc = [152,106,85,63, 43,31,25.1]
#tcp = [172,131,99, 70, 51, 45, 29.6]
dc = [102, 68, 54, 39, 21, 12.3, 8.4, 7.8]
rc = [152,106,85,63, 43,31, 29.4, 25.1]
tcp = [172,131,99, 70, 51, 45, 31.5,29.6]
for i in range(len(dc)):
    dc[i] += 10 + (6-i)

a=[]
b=[]
c=[]
#x=np.arange(1,8,0.1)
x=[]
y=[]

adc=sum(dc)/len(dc)
arc=sum(rc)/len(rc)
print(1-adc/arc)
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)#图框下边
ax.spines['left'].set_linewidth(bwith)#图框左边
ax.spines['top'].set_linewidth(bwith)#图框上边
ax.spines['right'].set_linewidth(bwith)#图框右边
plt.grid(b=True, linestyle="--", alpha=0.5,axis="both")

for i in range(3,800):
    x.append(i+0.5)
    y.append(1824/i)

for i in range(8):
    tcp[i]=tcp[i]*3
    rc[i]=rc[i]*3
    dc[i]=dc[i]*3
print(dc)
#for i in x:
#    y.append(132/(i-0.2))
width = [4,8,16,32,64,128,256,512]
for i in range(len(width)):
    width[i] = width[i]*0.25
for i in range(len(width)):
    a.append(pow(2,i+2)-width[i]/2)
    b.append(pow(2,i+2)+width[i]/2)
    if i==7:
        a[i]=512-512/4/2
        b[i]=512+512/4/2

save_path='./fig/3-1.png'
plt.xscale('log', base=2)
plt.xticks([i for i in [4,8,16,32,64,128,256,512]], ['4','8','16','32','64','128','256','300'])
plt.xlim((2.5,800))
plt.ylim((0,600))
plt.plot(x,y,color='red',linestyle='--',linewidth=4, label='Ideal JCT')
plt.bar(a,tcp,color='lightskyblue',width=width,label='TCP',hatch = '--', linewidth=2, edgecolor='black')
plt.bar(b,rc,color='orange',width=width,label='RC RDMA',hatch = '//', linewidth=2, edgecolor='black')
plt.legend(loc = 'upper right', fontsize = 20, frameon = False,  ncol = 1)
plt.xlabel('Scale', fontsize = fs)
plt.ylabel('Average Execution Time (s)', fontsize = fs)
plt.tick_params(labelsize = fs)
plt.savefig(save_path,bbox_inches='tight', pad_inches=0.05, dpi=800)
plt.show()
'''

s = [4,8,16,32,64,128,300]
save_path='./fig/fig6-13.jpg'
plt.xscale('log', base=2)
plt.ylim((0,600))
plt.xticks([i for i in [4,8,16,32,64,128,300]], ['4','8','16','32','64','128','300'])
for i in range(1,8):
    a.append(i)
plt.plot(s,tcp,label='TCP', linewidth=lw,marker='o', markersize=12)
plt.plot(s,rc,label='RC RDMA',linewidth=lw, marker='^', markersize=12)
plt.plot(s,dc,label='sparkRDMA', linewidth=lw,marker='s', markersize=12)
plt.legend(loc = 'upper right', fontsize = 18, frameon = False,  ncol = 1)
plt.xlabel('Scale', fontsize = fs)
plt.ylabel('Average JCT (s)', fontsize = fs)
plt.tick_params(labelsize = fs)
plt.savefig(save_path,bbox_inches='tight', pad_inches=0.05, dpi=800)
plt.show()
'''