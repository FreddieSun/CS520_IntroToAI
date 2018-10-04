import random
import numpy as np
from PIL import  Image

def createMaze(n, p):
    maze = np.zeros([n, n])
    for i in range(n):
        for j in range(n):
            b = random.uniform(0, 1)
            if b <= p:
                maze[i][j] = 1
            else:
                maze[i][j] = 0
    maze[0][0] = 0
    maze[n - 1][n - 1] = 0
    return maze

def drawmaze(maze):
    size=len(maze)
    mazedrown=Image.new('RGB',(size,size))
    mazex=mazedrown.load()
    for i in range(size):
        for j in range(size):
            if maze[i][j] == 0:
                color = 255
            else:
                color = 0
            mazex[i, j] = (color, color, color)
    mazedrown.show()
    return mazedrown

