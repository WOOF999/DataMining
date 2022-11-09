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

#make graph
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

#save data set
FILE=open('gene.txt')
READ=csv.reader(FILE,delimiter='\t')
for row in READ:
    DATA.append(row)


def selective_joining(pre_data,size):
    new_data=list()
   
    for edge1 in pre_data:
        for edge2 in pre_data:
            if pre_data.index(edge1)<pre_data.index(edge2):
                set1=set(edge1)
                set2=set(edge2)
                if len(set1&set2)==size-2:
                    if isClique(set1,set2):
                        new_data.append(set1|set2)
                        print("make new clique")
                        #print(new_data)
                        
    return new_data    


    
def isClique(set1,set2):
    sym_diff = list(set1 ^ set2)
    if sym_diff[1] in G[sym_diff[0]]:
        return True
    else:
        return False

    


    
def print_graph():
    for key,value in G.items():
            print("{} : {}".format(key,value))
            #print(len(value))

def print_dataset():
    print(DATA)

def main():
    print_graph()
    #print(DATA) 
    '''
    for edge in DATA:
        if "YBR112C" in edge:
            print(edge.index("YBR112C"))
            print(DATA.index(edge))

    '''
    initial_data=list(DATA)
    new_data=list()
    new_data=selective_joining(initial_data,3)
    print("elapsed time : ",end='')
    print(f"{time.time()-start:.6f} sec")


if __name__=="__main__":
    main()


