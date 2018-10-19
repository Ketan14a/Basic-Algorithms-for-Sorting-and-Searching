#insertion sort


data = []
n = int(input("Enter the number of elements to be sorted:"))
print("Enter %s numbers in randomly sorted order:" % str(n))
for i in range(n):
    data.append(int(input()))


for i in range(1,n):
    key = data[i]
    j=i-1
    while(j>=0 and data[j]>key):
        data[j+1] = data[j]
        j=j-1
    data[j+1]=key
    print("After iteration %s, the list is :-" %(i))
    for k in range(n):
        print(data[k])




print("The sorted list in ascending order is as follows:-")

for i in range(n):
    print(data[i])



        
    
