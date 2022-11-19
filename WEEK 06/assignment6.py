#2021245044 소프트웨어학부 서은하
import matplotlib.pyplot as plt
import numpy as np
import csv
import time
from collections import deque
import sys

#elapsed time
start=time.time()

#global variable
G=dict()
jaccard_index_list=list()
final_cluster=list()
vertex_list=list()
###checkehcekchekckehcke
density_threshold=0.6
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
    list2=list(G[sub2])
    list2.append(sub2)
    set2=set(list2)

    return float(len(set1.intersection(set2))/len(set1.union(set2)))

def BFS(graph, start):
    visited_nodes = []
    adjacency_nodes = deque([start])

    while adjacency_nodes:
        node = adjacency_nodes.popleft()
        if node not in visited_nodes:
            visited_nodes.append(node)
            adjacency_nodes.extend(graph[node])
    return visited_nodes

def check_BFS():
    isDisconnected=False
    visited_vertex=[]
    visited_vertex=BFS(G,vertex_list[0])
    print(calculate_density(visited_vertex))
    #if too slow.. make set?
    left_vertex = [x for x in vertex_list if x not in visited_vertex]
    while visited_vertex!=vertex_list:
        isDisconnected=True
        visited_vertex=visited_vertex+BFS(G,left_vertex[0])
        visited_vertex.sort()
        if visited_vertex==vertex_list:
            break
        left_vertex = [x for x in vertex_list if x not in visited_vertex]
        
def calculate_density(subGraph):
    vertex_num=len(subGraph)
    edge_num=0
    for node1 in range(vertex_num-1):
        for node2 in range(node1+1,vertex_num):
            if subGraph[node2] in G[subGraph[node1]]:
                edge_num+=1
    return 2*edge_num/(vertex_num*(vertex_num-1))

def check_jaccard_list():
    for set in jaccard_index_list:
        if set[2]==0:
            pass
        else:
            g_set=list(G[set[0]])
            if set[1] in g_set:
                #delete edge
                G[set[0]].remove(set[1])
                G[set[1]].remove(set[0])
                
                print(G)
            else:
                pass
            




def make_jaccard_index_list():
    temp=[]
    for key1 in G:
        for key2 in G:
            if key1 in G[key2]:
                temp.append(key1)
                temp.append(key2)
                temp.sort()
                temp.append(calculate_jaccard_index(key1,key2))
                tmp2=temp.copy()
                temp.clear()
                if tmp2 not in jaccard_index_list:
                    jaccard_index_list.append(tmp2)
    jaccard_index_list.sort(key=lambda x:x[2])
    print(jaccard_index_list)

def make_vertex_list():
    for key in G:
        vertex_list.append(key)
    vertex_list.sort()

def main():
    make_vertex_list()
    check_BFS()
    #make_jaccard_index_list()
    #check_jaccard_list()

    

if __name__=="__main__":
    main()