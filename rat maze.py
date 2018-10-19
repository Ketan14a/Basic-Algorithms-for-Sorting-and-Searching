# THE RAT MAZE PROBLEM VIA BACK-TRACKING

MAZE = [
         [1,1,1,0,0],
         [0,1,1,1,1],
         [0,1,1,1,0],
         [0,1,0,1,1],
         [0,1,1,0,1]
       ]



ANS =  [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]
       ]



def isSafe(maze,x,y):
    if(maze[y][x]==1):
        return True
    else:
        return False


def solveMaze(maze,x,y,sol):
    print("For x = ",x)
    print("For y = ",y,"\n")
    if(x==4 and y==4):
        sol[y][x]=1
        return True
    if(x==4 and y!=4):
         if(isSafe(maze,x,y)==True):
              sol[y][x]=1
              if(solveMaze(maze,x,y+1,sol)==True):
                  return True
            
       
         
    if(y==4 and x!=4):
        if(isSafe(maze,x,y)==True):
              sol[y][x]=1
              if(solveMaze(maze,x+1,y,sol)==True):
                  return True
        
                  
        
    if(isSafe(maze,x,y)==True):
        sol[y][x]=1
        if(solveMaze(maze,x+1,y,sol)==True):
            return True
        if(solveMaze(maze,x,y+1,sol)==True):
            return True
        sol[y][x]=0
        return False
    return False



result = solveMaze(MAZE,0,0,ANS)
if(result==True):
    print("THE SOLUTION TO THE MAZE IS AS FOLLOWS :- ")
    for i in ANS:
        print(i)
    
else:
    print("NO SOLUTION EXISTS FOR GIVEN MAZE")
    





