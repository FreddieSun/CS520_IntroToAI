from mazeCreator import createMaze
import numpy as np
import sys
import time
sys.setrecursionlimit(150000)

class parent:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def bfsmaze(maze):
    n = len(maze)
    color= np.zeros([n, n])
    path = []
    for i in range(n):
        path += [[]]
        for j in range(n):
            path[i] += [parent()]
    x=[0]
    y=[0]
    front=0
    end=1
    color[0][0] = 1
    next=[[0,1],[0,-1],[1,0],[-1,0]]
    while (front<end):
        for i in range(4):
            x_next=x[front]+next[i][0]
            y_next=y[front]+next[i][1]
            #next=node(x=x_next,y=y_next)
            #next.x=x_next
            #next.y=y_next
            if 0<=x_next<=n-1 and 0<=y_next<=n-1 and color[x_next][y_next]==0 and maze[x_next][y_next]==0:
                color[x_next][y_next]=1
                end+=1
                x.append(x_next)
                y.append(y_next)
                path[x_next][y_next].x=x[front]
                path[x_next][y_next].y=y[front]

        front+=1

        if x_next==n-1 and y_next==n-1:
            x.append(x_next)
            y.append(y_next)
            break
    z = list(zip(x, y))
    print('Number of nodes expanded in total:',len(z))
    print('Nodes expanded:',z)
    if (n-1,n-1) not in z:
        print('No path')
        sys.exit(0)

    return path
pathx=[]
pathy=[]
def getpath(x,y,path):

    if x == 0 and y == 0:
        return
    else:
        getpath(path[x][y].x, path[x][y].y,path)
        pathx.append(path[x][y].x)
        pathy.append(path[x][y].y)

def main():
    start=time.time()
    maze=createMaze(4, 0.2)
    n=len(maze)
    print('The maze is:','\n',maze)
    path=bfsmaze(maze)
    getpath(n-1,n-1,path)
    finalpath=list(zip(pathx,pathy))
    finalpath.append((n-1,n-1))
    print('The final path is',finalpath)
    print('The length of minimum path is',len(finalpath)-1)
    end=time.time()
    print('Running time is:',end-start,'s')

if __name__ == "__main__":
    main()



