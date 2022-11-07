#2021245044 소프트웨어학부 서은하
import matplotlib.pyplot as plt
import numpy as np
import csv
import time
import sys

#elapsed time
start=time.time()

#read csv data
#FILE=open('gene.txt')
FILE=open(sys.argv[1])
READ=csv.reader(FILE,delimiter='\t')

#declare
DATA=list()
Data_list=list()
Cluster_list=list()
previous_cluster=list()
MAX_DISTANCE=5

for row in READ:
    DATA.append(list(map(float,row)))

class Data:
    #index 0~499
    def __init__(self,index):
        self.point_index=index
        self.distance=dict()

    def set_distance(self,point):
        self.distance[point]=calculate_dist(self.point_index,point)

class Cluster:
    def __init__(self,id):
        self.id=id

    def append_point_to_cluster(self,point):
        self.cluster=list()
        self.cluster.append(point)    

def initialize_cluster():
    Cluster_list.clear()
    Data_list.clear()
    for index in range(500):
        Cluster_list.append(Cluster(index))
        Data_list.append(Data(index))

    for data in Data_list:
        for point2 in range(500):
            if point2!=data.point_index:
                data.set_distance(point2)

    for point in range(500):
        Cluster_list[point].append_point_to_cluster(point)

def calculate_dist(point1,point2):
    sum=0
    value1=np.array(DATA[point1])
    value2=np.array(DATA[point2])
    sub=value1-value2
    for index in range(len(sub)):
        sum+=sub[index]*sub[index]
    sum=np.sqrt(sum)
    return round(sum,3)
    

def make_new_cluster(cluster1,cluster2):
    new_cluster=Cluster(len(Cluster_list))

    new_cluster.cluster=cluster1.cluster+cluster2.cluster
    Cluster_list.remove(cluster1)
    Cluster_list.remove(cluster2)

    Cluster_list.append(new_cluster)

def get_closest_cluster_single():
    min_distance=5
    tmp_cluster1=None
    tmp_cluster2=None
    for cluster1 in Cluster_list:
        for cluster2 in Cluster_list:
            if cluster1!=cluster2:
                dist=single_link_distance(cluster1,cluster2)
                if dist>=MAX_DISTANCE:
                    continue 
                elif dist<min_distance:
                    min_distance=dist
                    tmp_cluster1=cluster1
                    tmp_cluster2=cluster2
    if min_distance<5:
        make_new_cluster(tmp_cluster1,tmp_cluster2)
    else:
        return

def get_closest_cluster_complete():
    min_distance=5
    tmp_cluster1=None
    tmp_cluster2=None
    for cluster1 in Cluster_list:
        for cluster2 in Cluster_list:
            if cluster1!=cluster2:
                dist=complete_link_distance(cluster1,cluster2)
                if dist>=MAX_DISTANCE:
                    continue 
                elif dist<min_distance:
                    min_distance=dist
                    tmp_cluster1=cluster1
                    tmp_cluster2=cluster2
    if min_distance<5:
        make_new_cluster(tmp_cluster1,tmp_cluster2)
    else:
        return

    
def single_link_distance(cluster1,cluster2):
    min_distance=5
    for point1 in cluster1.cluster:
        for point2 in cluster2.cluster:
            dist=Data_list[point1].distance[point2]
            #dist=calculate_dist(point1,point2)
            if dist<min_distance:
                min_distance=dist
    return min_distance
            

def complete_link_distance(cluster1,cluster2):
    max_distance=0
    for point1 in cluster1.cluster:
        for point2 in cluster2.cluster:
            dist=Data_list[point1].distance[point2]
            #dist=calculate_dist(point1,point2)
            if dist>max_distance:
                max_distance=dist
    return max_distance


#single_link
initialize_cluster()
for cluster in Cluster_list:
    previous_cluster.append(cluster)
get_closest_cluster_single()

while previous_cluster!=Cluster_list:
    previous_cluster.clear()
    for cluster in Cluster_list:
        previous_cluster.append(cluster)
    get_closest_cluster_single()
    #print("make new cluster...[single]\n")
    
#single link.txt
single_f=open('assignment4_output1.txt','w')

for cluster in Cluster_list: 
    single_f.write(str(len(cluster.cluster)))
    single_f.write(": ")
    for point in cluster.cluster:
        single_f.write(str(point))
        single_f.write(" ")
    single_f.write("\n")

single_f.close()
#print("file making success![single]")


#complete_link
initialize_cluster()
previous_cluster.clear()

for cluster in Cluster_list:
    previous_cluster.append(cluster)
get_closest_cluster_complete()

while previous_cluster!=Cluster_list:
    previous_cluster.clear()
    for cluster in Cluster_list:
        previous_cluster.append(cluster)
    get_closest_cluster_complete()
    #print("make new cluster...[complete]\n")
    



#complete link.txt
complete_f=open('assignment4_output2.txt','w')

for cluster in Cluster_list: 
    complete_f.write(str(len(cluster.cluster)))
    complete_f.write(": ")
    for point in cluster.cluster:
        complete_f.write(str(point))
        complete_f.write(" ")
    complete_f.write("\n")
    
complete_f.close()
#print("file making success![complete]")

print("elapsed time : ",end='')
print(f"{time.time()-start:.6f} sec")
