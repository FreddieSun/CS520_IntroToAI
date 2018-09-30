import random
import numpy as np
def createmaze(n,p):
    valuelist=[]
    for i in range(n*n):
        b=random.uniform(0,1)
        if b<=p:
            valuelist.append(1)
        else:
            valuelist.append(0)
    k=0
    maze=np.zeros([n,n])
    for i in range(n):
        for j in range(n):
            maze[i][j] = valuelist[k]
            k += 1
    maze[0][0]=0
    maze[n-1][n-1]=0
    return maze



