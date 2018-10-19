 #binomial coefficient using dynamic programming

def getC(n,k):
     if(k==n or k==0):
          
          return 1
     elif(flag[n][k]==1):
          return value[n][k]
     
     else:
          ans = getC(n-1,k-1)+getC(n-1,k)
          value[n][k]=ans
          flag[n][k]=1
          return ans
         
          


N = int(input("Enter N:"))
K = int(input("Enter K: "))
value = []
flag = []

for i in range(N+1):
     value.append([])
     flag.append([])
     for j in range(K+1):
          value[i].append([])
          flag[i].append([])
          flag[i][j]=0




          

Coeff = getC(N,K)


print("The Coefficient is ",Coeff)


     
