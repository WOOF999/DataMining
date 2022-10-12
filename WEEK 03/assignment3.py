#2021245044 서은하
import sys
from math import dist
import datetime
import numpy as np
import csv
from collections import defaultdict

#CONST VALUE
NUM_OF_DATA=500
K=10

#read csv data
FILE=open('gene.txt')
#f=open(sys.argv[1])
READ=csv.reader(FILE,delimiter='\t')

#declare
DATA=list()
DATA_FLOAT=list()
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
    return dist(point1,point2)

def get_closest_medoid(medoids,point):
    closest_medoid=0
    closest_distance=1000

    for medoid in medoids:
        distance=get_distance(point,DATA_FLOAT[medoid])
        if distance <closest_distance:
            closest_medoid=medoid
            closest_distance=round(distance,3)
    return closest_medoid,closest_distance

def update_medoids(clusters):
    for point1 in clusters:
        sumOfdistance=0.0
        for point2 in clusters:
            sumOfdistance+=get_distance(DATA_FLOAT[point1],DATA_FLOAT[point2])
        
        if sumOfdistance<max(medoids.values()):
            del medoids[max(medoids,key= lambda x: medoids[x])]
            medoids[point1]=round(sumOfdistance,3)
    return medoids

def reassigned_cluster(medoids):
    for point in range(len(DATA_FLOAT)):
        if point in medoids:
            continue
        else:
            closest_medoid,closest_distance=get_closest_medoid(medoids,DATA_FLOAT[point])
            clusters[closest_medoid].append(point)
    return clusters



#MAIN FUNC

print(initialize_medoids())
print(initialize_clusters())
print(update_medoids(clusters))