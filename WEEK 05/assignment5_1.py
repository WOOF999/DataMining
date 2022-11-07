#2021245044 소프트웨어학부 서은하
import matplotlib.pyplot as plt
import numpy as np
import csv
import time
import sys

#elapsed time
start=time.time()

count=0
DATA=list()
G=dict()

#read csv data
with open('gene.txt','r') as file:
    for line in file:
        n1,n2=line.strip().split('\t')
        try:
            G[n1].add(n2)
        except KeyError:
            G[n1]={n2}
        try:
            G[n2].add(n1)
        except KeyError:
            G[n2]={n1}


for key,value in G.items():
    print("{} : {}".format(key,value))




print("elapsed time : ",end='')
print(f"{time.time()-start:.6f} sec")



