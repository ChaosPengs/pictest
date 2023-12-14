# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:58:00 2023

@author: Lenovo
"""

import time
from threading import Thread
import matplotlib.pyplot as plt


def task(i):
    #print("另外开始一个子线程做任务啦")
    #time.sleep(10-i)  # 用time.sleep模拟任务耗时
    #print("子线程{}任务结束啦".format(i))
    pass

if __name__ == '__main__':
    print("这里是主线程")
    # 创建线程对象
    num = 200
    worker_num = 9
    non_worker_id = []
    t = []
    thread_id = []
    worker_id = []
    a = []
    b = []
    width = 0.6
    for i in range(num):
        t1 = Thread(target=task,args=(i,))
        t.append(t1)
    
    for i in range(1,worker_num+1):
        worker_id.append(0)
        non_worker_id.append(0)
        #a.append(i-width/2)
        #b.append(i+width/2)
        a.append(i)
        b.append(i)
        
    for thread in t:
        thread.start()
        #print(t1.ident)
        thread_id.append(thread.ident)
    #time.sleep(0.3)
    non_id = 0
    for tid in thread_id:
        index = tid%worker_num
        #print(tid,index)
        worker_id[index] += 1
        non_worker_id[non_id] += 1
        non_id = (non_id+1)%worker_num
    print(worker_id)
    print(non_worker_id)
    bwith=2
    save_path='./fig/fig6-10.jpg'
    plt.grid(b=True, linestyle="--", alpha=0.5,axis="both")
    fs=18
    ax = plt.gca()
    ax.spines['bottom'].set_linewidth(bwith)#图框下边
    ax.spines['left'].set_linewidth(bwith)#图框左边
    ax.spines['top'].set_linewidth(bwith)#图框上边
    ax.spines['right'].set_linewidth(bwith)#图框右边
    worker_id = [25, 17, 23, 30, 27, 20, 24, 19, 15]
    non_worker_id = [23, 23, 22, 22, 22, 22, 22, 22, 22]
    #plt.bar(a,worker_id, width=width, color = 'dodgerblue',label = 'Blocking',linewidth=2,edgecolor='black')
    plt.bar(b,non_worker_id, width=width, color = 'darkorange',label = 'Non-blocking',linewidth=2,edgecolor='black')
    plt.xlabel("Worker ID", fontsize = 16)
    plt.ylabel("Executors", fontsize = 18)
    plt.xticks([1,2,3,4,5,6,7,8,9])
    plt.ylim((10,35))
    plt.tick_params(labelsize = fs)
    plt.legend(loc = 'upper right', fontsize = 18, frameon = False,  ncol = 1)
    plt.savefig(save_path,bbox_inches='tight', pad_inches=0.05, dpi=800)