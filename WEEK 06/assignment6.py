#2021245044 소프트웨어학부 서은하
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
density_threshold=0.5
#(density) = (the number of edges) / (the number of nodes)
#jaccard index = A | B / A U B

#make graph
with open("gene.txt",'r') as file:
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
    make_vertex_list()
    visited_vertex=BFS(G,vertex_list[0])

    #if too slow.. make set?
    left_vertex = [x for x in vertex_list if x not in visited_vertex]
    
    if len(left_vertex)==0 and calculate_density(visited_vertex)>density_threshold:
        make_final_cluster(visited_vertex)
        return isDisconnected

    elif len(left_vertex)==1:
        delete_single_vertex(left_vertex)
        isDisconnected=True
        return isDisconnected

    visited_vertex.sort()
    while visited_vertex!=vertex_list:
        isDisconnected=True
        temp_vertex=BFS(G,left_vertex[0])
        if calculate_density(temp_vertex)>density_threshold:
            make_final_cluster(temp_vertex)
            return isDisconnected
        else:
            visited_vertex=visited_vertex+temp_vertex
        visited_vertex.sort()
        if visited_vertex==vertex_list:
            isDisconnected=False
            break
        left_vertex = [x for x in vertex_list if x not in visited_vertex]
    return isDisconnected


def delete_single_vertex(vertex):
    G.pop(vertex[0], None)   
        
def calculate_density(subGraph):
    vertex_num=len(subGraph)
    if vertex_num==1:
        return 0
    edge_num=0
    for node1 in range(vertex_num-1):
        for node2 in range(node1+1,vertex_num):
            if subGraph[node2] in G[subGraph[node1]]:
                edge_num+=1
    return 2*edge_num/(vertex_num*(vertex_num-1))

def calculate_jaccard_index(sub1,sub2):
    list1=list(G[sub1])
    list1.append(sub1)
    set1=set(list1)
    list2=list(G[sub2])
    list2.append(sub2)
    set2=set(list2)

    return float(len(set1.intersection(set2))/len(set1.union(set2)))  

def make_jaccard_index_list():
    jaccard_index_list.clear()
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



def check_jaccard_list():
    make_jaccard_index_list()
    for set in jaccard_index_list:
        if set[2]==0:
            pass
        else:
            if not G:
                return
            g_set=list(G[set[0]])
            if set[1] in g_set:
                #delete edge
                G[set[0]].remove(set[1])
                G[set[1]].remove(set[0])
                
                check=check_BFS()
                if check:
                    return
                
            else:
                pass

def make_vertex_list():
    vertex_list.clear()
    for key in G:
        vertex_list.append(key)
    vertex_list.sort()

def make_final_cluster(subGraph):
    final_cluster.append(subGraph)
    for key in subGraph:
        G.pop(key, None)   

def main():
    make_vertex_list()
    check_BFS()

    while G:
        check_jaccard_list()
        print(len(G))
        print(final_cluster)
  
    cluster_f=open('assignment6output.txt','a')
    for cluster in final_cluster:
        cluster_f.write(str(len(cluster)))
        cluster_f.write(": ")
        for point in cluster:
            cluster_f.write(point)
            cluster_f.write(" ")
        cluster_f.write("\n")
    cluster_f.close()
    print("elapsed time : ",end='')
    print(f"{time.time()-start:.6f} sec")

    

if __name__=="__main__":
    main()