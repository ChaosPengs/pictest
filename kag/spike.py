# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 21:00:02 2023

@author: Lenovo
"""


import numpy as np
import matplotlib.pyplot as plt
import csv

filename = './apppc2.csv'
point_sz = 30
bwith=2
#save_path = './taskspike.jpg'
#save_path = './fig/fig3-3.jpg'
save_path = './fig/3-3.png'
fs = 18
xtick = [10,20,30, 40, 50]
ytick = [20,40,60,80,100,120]
data = []
x = []
colors=[]
with open(filename, "r", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        data.append(float(row[0]))
        x.append(float(row[1]))

for xi, yi in zip(x, data):
    if yi >= 40:
        colors.append('red')
    else:
        colors.append('blue')

#plt.figure(figsize = (5, 3))
ax = plt.gca()
ax.spines['bottom'].set_linewidth(bwith)#图框下边
ax.spines['left'].set_linewidth(bwith)#图框左边
ax.spines['top'].set_linewidth(bwith)#图框上边
ax.spines['right'].set_linewidth(bwith)#图框右边
plt.grid(b=True, linestyle="--", alpha=0.5,axis="both")
plt.scatter(x,data,color = colors, s = point_sz)

plt.ylim((15,120))
plt.xlim((5,55))
#plt.legend(loc = 'upper right', fontsize = 12, frameon = False,  ncol = 2)


plt.xticks(xtick)
plt.yticks(ytick)
plt.xlabel('Data Length (MB)', fontsize = fs)
plt.ylabel('Time (s)', fontsize = fs)
plt.tick_params(labelsize = fs)
plt.savefig(save_path,bbox_inches='tight', pad_inches=0.05, dpi=800)
plt.show()