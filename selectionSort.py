#selection sort

data = []

n = int(input("Enter the number of elements to be sorted:"))
print("Enter %s numbers in randomly sorted order:" % str(n))

for i in range(n):
    data.append(int(input()))


for i in range(n):
    for j in range(i+1,n):
        if(data[i]>data[j]):
            temp=data[i]
            data[i]=data[j]
            data[j]=temp
    print("After iteration %s, the list is :-" % (i+1))
    for k in range(n):
        print(data[k])




print("The sorted list is as follows:")

for i in range(n):
    print(data[i])

