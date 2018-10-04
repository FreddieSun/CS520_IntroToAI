from mazeCreator import createMaze,drawmaze
import numpy as np
import sys
import time
from PIL import Image
sys.setrecursionlimit(150000)

class parent:     #create a parent class, for finding the minimum path
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def bfsmaze(maze):
    n = len(maze)
    color= np.zeros([n, n])          #mark whether a node is visited
    path = []
    for i in range(n):
        path += [[]]
        for j in range(n):
            path[i] += [parent()]    #create a n*n two dimensional array, store each node's parent node
    x=[0]     #the x coordinate of the node
    y=[0]     #the y coordinate of the node
    front=0   #the beginning of the queue
    end=1     #the end of the queue
    color[0][0] = 1
    next=[[-1,0],[0,1],[0,-1],[1,0]]  #go left,go down,go up,go right
    while (front<end):
        for i in range(4):
            x_next=x[front]+next[i][0]  #bfs the node at the beginning of the queue
            y_next=y[front]+next[i][1]
            if 0<=x_next<=n-1 and 0<=y_next<=n-1 and color[x_next][y_next]==0 and maze[x_next][y_next]==0: #check if the next-visit-node is in the maze and can be visited
                color[x_next][y_next]=1  #mark the node as visited
                end+=1                   #append the end
                x.append(x_next)         #add the qualified node in the queue
                y.append(y_next)
                path[x_next][y_next].x=x[front] #in the path array, mark the node's parent node.
                path[x_next][y_next].y=y[front]

        front+=1  #start to bfs the next node in the queue.

        if x_next==n-1 and y_next==n-1: #if arrive at the destination, stop bfs.
            x.append(x_next)
            y.append(y_next)
            break
    z = list(zip(x, y))  #combine the x coordinate and y coordinate togther to get the final result.
    print('Number of nodes expanded in total:',len(z))
    print('Nodes expanded:',z)
    if (n-1,n-1) not in z:  #if the destination not been visited, then there's no solution.
        print('No path')
        sys.exit(0)

    return path  #return the path array as the result.
pathx=[]
pathy=[]
def getpath(x,y,path):  #from the destination, use a recursion way to find the minimum path.

    if x == 0 and y == 0:  #reach the start, path found
        return
    else:
        getpath(path[x][y].x, path[x][y].y,path) #path[x][y] is the parent of the (x,y). Use the recursion way to continue find the path.
        pathx.append(path[x][y].x)
        pathy.append(path[x][y].y)

def main():
    start=time.time() #start counting time
    maze=createMaze(290, 0.1)
    n=len(maze)
    print('The maze is:','\n',maze)
    mazedrown = drawmaze(maze)
    path=bfsmaze(maze)
    getpath(n-1,n-1,path)
    finalpath=list(zip(pathx,pathy))
    finalpath.append((n-1,n-1))   #get the final path
    print('The final path is',finalpath)
    print('The length of minimum path is',len(finalpath)-1)
    end=time.time()  #stop counting time
    print('Running time is:',end-start,'s')
    mazex=mazedrown.load()
    for i in finalpath:   #draw the path
        mazex[i]=(134,205,133)
    mazedrown.show()
    mazedrown.save('maze.png')  #save the final result.

if __name__ == "__main__":
    main()



