#for loop
for i in range(1,13):
    print(i,"월의 데이터입니다.")

for i in range(5):
    for j in range(3):
        print("i is :",i,"j is :",j)

v= False
for i in range(5):
    for j in range(5):
        if v is False:
            print("*",end=" ")
            v=True
        else:
            print("-",end=" ")
            v=False
    print()


#while loop
i=1
while i<=12:
    print(i,"month data")
    i+=1

#list
sale=[80,60,22,50,75]
print("current data is : ", sale)

sale.append(100)
print("current data is : ", sale)

sale.insert(2,25)
print("current data is : ", sale)

del sale[0]
print("current data is : ", sale)

sale.remove(22)
print("current data is : ", sale)