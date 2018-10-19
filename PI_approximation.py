import random
import math

putPoint = random.randint
root = math.sqrt

c_inside = 0
c_total = 0


for i in range(100000):
    x = putPoint(0,1000)
    y = putPoint(0,1000)

    d = root((x-500)*(x-500) + (y-500)*(y-500))

    if(d>500):
        c_total = c_total+1
    else:
        c_total = c_total+1
        c_inside = c_inside+1



PI = (c_inside/c_total)*4

print("The approximate value of PI obtained is ",PI)

