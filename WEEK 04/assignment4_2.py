import matplotlib.pyplot as plt
import numpy as np
import csv
#fake example data
#read csv data
FILE=open('gene.txt')

READ=csv.reader(FILE,delimiter='\t')

#declare
DATA=list()
DATA_FLOAT=list()


for row in READ:
    DATA.append(row)

for row in range(500):
    DATA_FLOAT.append(list(map(float,DATA[row])))



#list of arrays containing all data


#calculate 2d indicators
def indic(DATA_FLOAT):
    #alternatively you can calulate any other indicators
    max = np.max(DATA_FLOAT, axis=1)
    min = np.min(DATA_FLOAT, axis=1)
    return max, min

x,y = indic(DATA_FLOAT)
plt.scatter(x, y, marker='x')
plt.show()