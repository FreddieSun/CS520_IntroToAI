from mazeCreator import createMaze
import numpy as np
import sys

def bfsmaze(maze):
    n = len(maze)
    color= np.zeros([n, n])
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
            if 0<=x_next<=n-1 and 0<=y_next<=n-1 and color[x_next][y_next]==0 and maze[x_next][y_next]==0:
                color[x_next][y_next]=1
                end+=1
                x.append(x_next)
                y.append(y_next)
        front+=1
        if x_next==n-1 and y_next==n-1:
            x.append(x_next)
            y.append(y_next)
            break

    if x[len(x)-1] != n-1 or y[len(y)-1] != n-1:
        print('No path')
        sys.exit(0)
    print(x)
    print(y)

def main():
    maze=createMaze(6, 0.3)
    print(maze)
    bfsmaze(maze)

if __name__ == "__main__":
    main()



