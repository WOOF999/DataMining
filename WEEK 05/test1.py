#2021245044 소프트웨어학부 서은하
import matplotlib.pyplot as plt
import numpy as np
import csv
import time
import sys

count=0
DATA=list()

#read csv data
FILE=open('gene.txt')
#FILE=open(sys.argv[1])
READ=csv.reader(FILE,delimiter='\t')
for row in READ:
    DATA.append(row)
    count+=1
#elapsed time
start=time.time()


class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

    # Print the graph
    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


if __name__ == "__main__":
    V = count

    # Create graph and edges
    graph = Graph(V)

    #for row in DATA:
    #    tmp1=row[0]
    #    tmp2=row[1]
    #    graph.add_edge(tmp1,tmp2)

    #graph.print_agraph()


print("elapsed time : ",end='')
print(f"{time.time()-start:.6f} sec")



