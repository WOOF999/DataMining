#2021245044 서은하
import pandas as pd
import sys
import math

import datetime

def calculate_euclid(object,means):
    euclid=[]
   
    for index in range(10):
        sum=0
        for col in range(len(df.columns)):
            z=object[col]-means.loc[index][col]
            sum+=(z*z)
        euclid.append(round(math.sqrt(sum)))
               
    tmp=min(euclid)
    return euclid.index(tmp)    

def make_new_cluster(centeroid):
    cluster = [[],[],[],[],[],[],[],[],[],[]]
    for row in range(len(df)):
        cluster_index=calculate_euclid(df.loc[row],centeroid)
        cluster[cluster_index].append(row)
    return cluster

def recalculate_centeroid(cluster): 
    for i in range(10):
        means = [0 for i in range(len(df.columns))]
        for object in cluster[i]:
            for col in range(len(df.columns)):
                means[col]+=df.loc[object][col]
        for col in range(len(df.columns)):
            means[col]/=len(cluster[i])
            means[col]=round(means[col],3)
            centeroid.loc[i][col]=means[col]
    return centeroid


df=pd.read_csv(sys.argv[1],sep='\t',header=None)

k=10

centeroid=pd.DataFrame(index=range(0,k),columns={0,1,2,3,4,5,6,7,8,9,10,11})

count=0 #0~499

for cluster_index in range(k):
    means = [0 for i in range(len(df.columns))]
    for i in range(50):
        for col in range(len(df.columns)):
            means[col]+=df.loc[count][col]
        count+=1
        

    for col in range(len(df.columns)):
        means[col]/=50
        centeroid.loc[cluster_index][col]=means[col]
    

        
start=datetime.datetime.now()
check=0
while check!=1:
    pre_centeroid=centeroid.copy()
    new_cluster=make_new_cluster(centeroid)
    print(new_cluster)
    centeroid=recalculate_centeroid(new_cluster)
    print(centeroid)
    if pre_centeroid.equals(centeroid):
        check=1

for i in range(len(new_cluster)):
    print(len(new_cluster[i]),":",new_cluster[i])



end=datetime.datetime.now()
print(end-start)

del df