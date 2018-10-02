import numpy as np
from mazeCreator import createMaze
import sys
sys.setrecursionlimit(150000)

path = ''
shortestPath = ''

def dfs(x, y, maze):
    global path
    global shortestPath

    N = len(maze)
    # beyond the grid
    if x < 0 or y < 0 or x > N - 1 or y > N - 1:
        return

    # visited
    if maze[x][y] == 1:
        return

    # arrive the destination
    if x == N - 1 and y == N - 1:
        path = path + '(' + str(x) + ')' + '(' + str(y) + ')' + '-'
        print('path is :' + path)
        if len(shortestPath) == 0 or len(shortestPath) >= len(path):
            shortestPath = path
        return

    temp = path
    path = path + '(' + str(x) + ')' + '(' + str(y) + ')' + '-'

    maze[x][y] = 1
    # right
    dfs(x+1, y, maze)
    # down
    dfs(x, y+1, maze)
    # up
    dfs(x, y-1, maze)
    # left
    dfs(x-1, y, maze)

    # dead path, clear this grid and undo the path
    maze[x][y] = 0
    path = temp


def main():
    # Generate the maze with size N*N and p
    maze=createMaze(5000, 0.2)
    print(maze)

    dfs(0,0,maze)

    if len(shortestPath) == 0:
        print('No path')
    else:
        print('shortestPath is :'+ shortestPath)


if __name__ == "__main__":
    main()