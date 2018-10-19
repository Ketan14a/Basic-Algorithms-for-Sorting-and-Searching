def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

     

      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

data = []

n = int(input("Enter the number of elements to be sorted:"))

print("Enter %s numbers in randomly sorted order:" % str(n))
for i in range(n):
    data.append(int(input()))

shellSort(data)


print("The sorted list is as follows:-")

for i in range(n):
    print(data[i])

