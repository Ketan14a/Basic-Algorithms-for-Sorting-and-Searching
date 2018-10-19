s1 = input("Enter s1:")
s2 = input("Enter s2:")

def LCS(lx,ly):
    if(lx==0 or ly==0):
        return 0
    elif(s1[lx-1]==s2[ly-1]):
        return (LCS(lx-1,ly-1)+1)
    else:
        return max(LCS(lx-1,ly),LCS(lx,ly-1))



cost = LCS(len(s1),len(s2))

print("THE COST OF LCS IS " + str(cost))



                
                
