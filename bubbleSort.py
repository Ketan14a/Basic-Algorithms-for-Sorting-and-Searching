#Bubble sort

data = []

n = int(input("Enter the number of elements to be sorted:"))

print("Enter %s numbers in randomly sorted order:" % str(n))

for i in range(n):
    data.append(int(input()))


for i in range(n):
    j=n-1
    while(j>i):
        if(data[j]<data[j-1]):
            temp=data[j]
            data[j]=data[j-1]
            data[j-1]=temp
        j=j-1
    print("after iteration %s, the list is :-" % str(i+1))
    for k in range(n):
        print(data[k])


        

print("The sorted list in ascending order is as follows:")

for i in range(n):
    print(data[i])





