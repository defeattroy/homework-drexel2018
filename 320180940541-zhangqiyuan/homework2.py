import re
import pandas as pd
import time
from subprocess import Popen, PIPE,DEVNULL
import unicodedata
import matplotlib.pyplot as plt
import numpy as np
def get_timestamp():
    repo = 'C:/Users/Administrator/linux-stable'
    #cmd = ["git", "log",'--pretty=format:"%cd"','v4.4']
    cmd = 'git log -1 --pretty=format:"%cd" v4.4'
    p = Popen(cmd, cwd=repo,stdout=PIPE,shell=True)
    data, res = p.communicate()
    print(data.decode())

def get_list(versions,repo):
    total_time_stamp_list=[]
    for version in versions:
        cmd='git tag | grep {} | sort -n -k3 -t"."'.format(version)
        p=Popen(cmd,cwd=repo,stdout=PIPE,shell=True)
        data,res=p.communicate()
        data=data.decode('latin').encode('utf8').decode('utf8').split("\n")
        time_stamp_list=[]
        for v in data:
            cmd_1 = 'git log -1 --pretty=format:"%ct" {}'.format(v)
            p = Popen(cmd_1, cwd=repo,stdout=PIPE,shell=True)
            time_stamp, res = p.communicate()
            time_stamp=int(time_stamp.decode('latin').encode('utf8').decode('utf8'))
            #time_stamp=("%e" %int(time_stamp))
            #value=time.mktime(time.strptime(time_stamp,'%Y-%m-%d %H:%M:%S'))
            time_stamp_list.append(time_stamp)
        total_time_stamp_list.append(time_stamp_list)
    print(total_time_stamp_list)
    return(total_time_stamp_list)
   

def draw_picture(total_time_stamp_list):
    count_value=0
    for i in total_time_stamp_list:
        j=[]
        for a in range(len(i)):
            j.append(count_value)
        count_value=count_value+1    	    
        #plt.scatter(i,j)
        #plt.xticks(i,[1.42e+09,1.43e+09,1.44e+09,1.45e+09,1.46e+09,1.47e+09,1.48e+09,1.49e+09])
        #plt.yticks(j,[0,2,4,6,8,10])
        plt.xlim(1.42e+09,1.49e+09)
        #plt.ylim(0,10)
        plt.xlabel('seconds')
        plt.ylabel('patchlevel')
        plt.scatter(i,j)
    plt.show()        			
		
repo = 'C:/Users/Administrator/linux-stable'
versions=['v4.1','v4.2','v4.3','v4.4','v4.5','v4.6','v4.7','v4.8','v4.9','v4.10']
#versions=['v4.4']
total_time_stamp_list=get_list(versions,repo)
draw_picture(total_time_stamp_list)

