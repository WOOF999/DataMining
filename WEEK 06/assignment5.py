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
with open(sys.argv[1],'r') as file:
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
#FILE=open('gene.txt')
FILE=open(sys.argv[1])
READ=csv.reader(FILE,delimiter='\t')
for row in READ:
    DATA.append(row)


def selective_joining(pre_data,size):
    new_data=list()
    for edge_num in range(len(pre_data)-1):
        for edge_num2 in range(edge_num+1,len(pre_data)):
            set1=set(pre_data[edge_num])
            set2=set(pre_data[edge_num2])
            union_set=set1|set2
            if len(set1&set2)==size-2 and union_set not in new_data:
                if isClique(set1,set2):
                    new_data.append(set1|set2)            
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

def print_dataset():
    print(DATA)

def main():
   
   #initialize
    initial_data=list(DATA)
    pre_data=initial_data.copy()
    new_data=list()
    new_data=selective_joining(initial_data,3)

    num=4
    while pre_data!=new_data:
        #print(".....check size-"+str(num)+" cliques.....")
        pre_data.clear()
        pre_data=new_data.copy()
        new_data=selective_joining(new_data,num)

        if num>=8:
            cluster_f=open('assignment5_output.txt','a')
            for cluster in new_data:
                cluster_f.write(str(len(cluster)))
                cluster_f.write(": ")
                for point in cluster:
                    cluster_f.write(point)
                    cluster_f.write(" ")
                cluster_f.write("\n")
        num+=1

    cluster_f.close()
    
    print("elapsed time : ",end='')
    print(f"{time.time()-start:.6f} sec")


if __name__=="__main__":
    main()


