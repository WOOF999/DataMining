#2021245044 소프트웨어학부 서은하
import matplotlib.pyplot as plt
import numpy as np
import csv
import time
import sys

#elapsed time
start=time.time()

#global variable
DATA=list()
G=dict()
density_threshold=0.4
#(density) = (the number of edges) / (the number of nodes)
#jaccard index = A | B / A U B

#make graph
with open("test.txt",'r') as file:
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

def calculate_jaccard_index(sub1,sub2):
    list1=list(G[sub1])
    list1.append(sub1)
    set1=set(list1)
    print(set1)
    list2=list(G[sub2])
    list2.append(sub2)
    set2=set(list2)
    print(set2)
    return float(len(set1.intersection(set2))/len(set1.union(set2)))


def calculate_density(subGraph):
    pass


def main():
    print(G)
    for key in G:
        for key2 in G:
            if key!=key2:
                print(calculate_jaccard_index(key,key2))



if __name__=="__main__":
    main()