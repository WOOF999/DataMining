#2021245044 소프트웨어학부 서은하
import matplotlib.pyplot as plt
import numpy as np
import csv
import time
import sys

#elapsed time
#start=time.time()
class Graph:
    def __init__(self):
        self.graph={}

    def addInfo(self,startV,endVs):
        self.graph[startV]=endVs

    def addEdge(self,startV,endV):
        self.graph[startV].append(endV)
    
    def addVertex(self,V):
        self.graph[V]=[]


count=0
DATA=list()
G=dict()
#read csv data
FILE=open('gene.txt')
#FILE=open(sys.argv[1])
READ=csv.reader(FILE,delimiter='\t')
for row in READ:
    DATA.append(row)
    count+=1

for vertex in DATA:
    G[vertex[0]]=vertex[1]



print(G)