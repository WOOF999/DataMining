#2021245044 서은하
import sys
from math import dist
import time
import numpy as np
import csv
from collections import defaultdict

#elapsed time
start=time.time()

#CONST VALUE
NUM_OF_DATA=500
K=10

#read csv data
#FILE=open('gene.txt')
FILE=open(sys.argv[1])
READ=csv.reader(FILE,delimiter='\t')

#declare
DATA=list()
DATA_FLOAT=list()
pre_medoids=dict()
medoids=dict()
clusters=defaultdict(list)

for row in READ:
    DATA.append(row)

for row in range(NUM_OF_DATA):
    DATA_FLOAT.append(list(map(float,DATA[row])))

def initialize_medoids():   
    for point1 in range(len(DATA_FLOAT)):
        sumOfdistance=0.0
        for point2 in range(len(DATA_FLOAT)):
            sumOfdistance+=get_distance(DATA_FLOAT[point1],DATA_FLOAT[point2])
        if len(medoids)<K:
            medoids[point1]=round(sumOfdistance,3)
        else:
            if sumOfdistance<max(medoids.values()):
                del medoids[max(medoids,key= lambda x: medoids[x])]
                medoids[point1]=round(sumOfdistance,3)
    return medoids

def initialize_clusters():
    closest_medoid=0
    closest_distance=0.0
    for point in range(len(DATA_FLOAT)):
        if point in medoids:
            continue
        else:
            closest_medoid,closest_distance=get_closest_medoid(medoids,DATA_FLOAT[point])
            clusters[closest_medoid].append(point)
    return clusters
 
def get_distance(point1,point2):
    sum=0
    value1=np.array(point1)
    value2=np.array(point2)
    sub=value1-value2
    for index in range(len(sub)):
        sum+=sub[index]*sub[index]
    sum=np.sqrt(sum)
    return sum

def get_closest_medoid(medoids,point):
    closest_medoid=0
    closest_distance=1000

    for medoid in medoids:
        distance=get_distance(point,DATA_FLOAT[medoid])
        if distance <closest_distance:
            closest_medoid=medoid
            closest_distance=round(distance,3)
    return closest_medoid,closest_distance

def calculate_pre_medoids(clusters):  
    pre_medoids.clear()
    for key in clusters:
        sumOfdistance=0.0
        sumOfdistance_min=1000
        for value in clusters[key]:
            sumOfdistance+=get_distance(DATA_FLOAT[key],DATA_FLOAT[value])
        if sumOfdistance<sumOfdistance_min:
            sumOfdistance_min=sumOfdistance
            pre_medoids[key]=round(sumOfdistance,3)
    return pre_medoids


def update_medoids(pre_medoids,clusters):
    tmp_medoids=dict()
    new_medoids=dict()
    for key in clusters:
        for value1 in clusters[key]:
            sumOfdistance=0.0
            for value2 in clusters[key]:
                sumOfdistance+=get_distance(DATA_FLOAT[value1],DATA_FLOAT[value2])
            if sumOfdistance<pre_medoids[key]:
                tmp_medoids[value1]=round(sumOfdistance,3)
        if not tmp_medoids:
            new_medoids[key]=pre_medoids[key]
        else:
            new_medoids[min(tmp_medoids,key= lambda x: tmp_medoids[x])]=min(tmp_medoids.values())
            tmp_medoids.clear()
    return new_medoids

def reassigned_cluster(medoids):
    clusters.clear()
    for point in range(len(DATA_FLOAT)):
        if point in medoids:
            continue
        else:
            closest_medoid,closest_distance=get_closest_medoid(medoids,DATA_FLOAT[point])
            clusters[closest_medoid].append(point)
    return clusters



#MAIN FUNC

#initailize medoids and clusters
initialize_medoids()
initialize_clusters()
calculate_pre_medoids(clusters)

new_medoids=update_medoids(pre_medoids,clusters)
clusters=reassigned_cluster(new_medoids)
pre_medoids=calculate_pre_medoids(clusters)

while new_medoids!=pre_medoids:
    new_medoids=update_medoids(pre_medoids,clusters)
    clusters=reassigned_cluster(new_medoids)
    pre_medoids=calculate_pre_medoids(clusters)
    
print("elapsed time : ",end='')
print(f"{time.time()-start:.4f} sec")

#print "assignment3_output.txt"
sys.stdout=open('assignment3_output.txt','w')

for key in clusters:
    cluster_size=len(clusters[key])+1
    print(cluster_size,end='')
    print(": ",end='')
    print(key,end=' ')
    for point in clusters[key]:
        print(point,end=' ')
    print()

sys.stdout.close()