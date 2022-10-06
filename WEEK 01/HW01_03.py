import csv
import matplotlib.pyplot as plt

f= open('seoul.csv','r',encoding='cp949')
data=csv.reader(f,delimiter=',')
next(data)
month=[[],[],[],[],[],[],[],[]]
print(data)
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

