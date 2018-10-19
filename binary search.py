data = []
flag=0

n = int(input("Enter the number of elements:"))
print("Enter %s numbers:" % str(n))

for i in range(n):
    data.append(int(input()))


sv = int(input("Enter the search value:"))
data.sort()
print(data)


def Bsearch(data,low,high):
    mid = int((low+high)/2)
    if(sv == data[mid]):
        print("gone at flag")
        flag=1;
        
        
    elif(sv > data[mid]):
        #data=data[mid:]
        print("sv > d[mid]")
        Bsearch(data,mid+1,high)
    else:
        print("sv < d[mid]")
        Bsearch(data,low,mid)
    
        
result = Bsearch(data,0,n-1)

if(flag == 1):
    print("%s found in the list " % str(sv))
else:
    print("%s not found in the list" % str(sv))
