data = []
flag=0

n = int(input("Enter the number of elements:"))
print("Enter %s numbers:" % str(n))

for i in range(n):
    data.append(int(input()))


sv = int(input("Enter the search value:"))

for i in range(n):
    if(data[i] == sv):
        flag=1
        break


if(flag==1):
    print("%s found in the list after %s iterations." % (str(sv),str(i+1)))

else:
    print("%s not found in the list" % str(sv))


        
