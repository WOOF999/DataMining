import csv
import matplotlib.pyplot as plt

#01
f= open('seoul.csv','r',encoding='cp949')
data=csv.reader(f,delimiter=',')
next(data)
high_temp=[]
low_temp=[]

for row in data:
    print(row)
    check=1
    for r in row:
        if r=='':
            check=0
    if check==1:
        if row[2].split('-')[1]=='08':
            high_temp.append(float(row[4]))
            low_temp.append(float(row[6]))

plt.plot(high_temp,'red',label='highest temp')
plt.plot(low_temp,'blue',label='lowest temp')

plt.xlabel('day')
plt.ylabel('temperature')
plt.title('August')
plt.legend()
plt.show()

#02
f= open('seoul.csv','r',encoding='cp949')
data=csv.reader(f,delimiter=',')
next(data)

august=[]
january=[]

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
plt.hist(august,bins=ag,color='red',label='August')
plt.hist(january,bins=jn,color='blue',label='January')
plt.xlabel('temperature')
plt.ylabel('number of days')
plt.title('January and August')
plt.legend()
plt.show()

#03

f= open('seoul.csv','r',encoding='cp949')
data=csv.reader(f,delimiter=',')
next(data)

month=[[],[],[],[],[],[],[],[]]
for row in data:
    print(row)
    check=1
    for r in row:
        if r=='':
            check=0
    if check==1:
        mnth=int(row[2].split('-')[1])
        month[mnth-1].append(float(row[3]))
            

plt.boxplot(month)
plt.xlabel('month')
plt.ylabel('temperature')
plt.title('January to August')
plt.legend()
plt.show()

f.close()