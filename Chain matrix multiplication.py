p = [0,0,0,0,0]
f = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
m = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
k = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

cost  = 0

def exp(i,j):
    if(i==j):
        print(i)
    else:
         print("(")
         exp(i,k[i][j-1]);
         exp(k[i][j-1]+1,j);
         print(")")


def getCost(i,j):
    k=0
    Min=100000
    ans=0

    if(i==j):
        return 0
    if(f[i][j-1]==1):
        return m[i][j-1]
    x=j-1
    for K in range(i,x):
        ans = getCost(i,K) + getCost(K+1,x) + (p[i-1]*p[x]*p[K]);
        if(ans<Min):
            Min = ans
            k[i][j] = K;

    m[i][x]=Min
    f[i][x]=1
    return Min


p[0] = int(input("Enter p0:"))
p[1] = int(input("Enter p1:"))
p[2] = int(input("Enter p2:"))
p[3] = int(input("Enter p3:"))
p[4] = int(input("Enter p4:"))


for i in range(4):
    for j in range(4):
        if(i<=j):
            m[i][j]=0
            f[i][j]=0
        if(i>j):
            m[i][j]=-64
            f[i][j]=-64

cost = getCost(1,4)
print("The cost is %s " % str(cost))
print("The matrices should be multiplied as :-")
exp(1,4)

    
        


            
        
