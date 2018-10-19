#ASSEMBLY LINE SCHEDULING

T = [[7,4,5],[9,2,8]]
A = [[4,5,3,2],[2,10,1,4]]
E = [10,12]
X = [18,7]



min = 1000000

def F1(j):
    
    if(j==0):
        sum=E[0]+A[0][0]
        return sum
    else:
        ans1=F1(j-1)+A[0][j]
        ans2=F2(j-1)+T[1][j-1]+A[0][j]
        if(ans1<ans2):
            return ans1
        else:
            return ans2
        


def F2(j):

    if(j==0):
        sum = E[1] + A[1][0]
        return sum
    else:
        ans1=F1(j-1)+T[0][j-1]+A[1][j]
        ans2=F2(j-1)+A[1][j]
        if(ans1<ans2):
            return ans1
        else:
            return ans2
        




path1 = F1(3)
path2 = F2(3)

tc1 = path1 + X[0]
tc2 = path2 + X[1]

if(tc1<tc2):
    TC = tc1
else:
    TC = tc2


print("The minimum cost is ", TC)

                
                

        
        


