import csv
import pandas as pd
import matplotlib.pyplot as plt

f=open('Seoul.csv','r')
reader = csv.reader(f)
count=0
for line in reader:
    print(line)
    count+=1
    
print("\n\n\n\n\n",count)
data=pd.DataFrame(reader)
data.head()
data.dropna(axis=0,how='any')
count=0
for line in data:
    print(line)
    count+=1
print("\n\n\n\n\n",count)
f.close()

xval=[1,2,3,4]
yval=[1,4,9,16]

plt.plot(xval,xval,color='b',label='y=x')
plt.plot(xval,yval,color='r',label='y=x**2')

plt.xlabel('x')
plt.ylabel('y')
plt.title('graph')
plt.legend()
plt.show()
