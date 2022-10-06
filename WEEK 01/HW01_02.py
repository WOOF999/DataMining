import csv
import matplotlib.pyplot as plt

f= open('seoul.csv','r',encoding='cp949')
data=csv.reader(f,delimiter=',')
next(data)
august=[]
january=[]
print(data)
for row in data:
    print(row)
    check=1
    for r in row:
        if r=='':
            check=0
    if check==1:
        if row[2].split('-')[1]=='08':
            august.append(float(row[4]))
        if row[2].split('-')[1]=='01':
            january.append(float(row[4]))
ag=len(august)
jn=len(january)
print(ag,jn)
plt.hist(august,bins=ag,color='red',label='August')
plt.hist(january,bins=jn,color='blue',label='January')
plt.xlabel('temperature')
plt.ylabel('number of days')
plt.title('January and August')
plt.legend()
plt.show()


