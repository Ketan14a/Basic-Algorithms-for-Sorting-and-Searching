# Quick sort




def quicksort(myList, start, end):
    if start < end:
        pivot = partition(myList, start, end)
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)
    return myList



def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right

n = int(input("Enter the number of elements to be sorted:"))
mylist=[]
print("Enter %s numbers in randomly sorted order:" % str(n))
for i in range(n):
    mylist.append(int(input()))

mylist = quicksort(mylist,0,n-1)


print("The sorted list is as follows:-")

for i in range(n):
    print(mylist[i])
            
