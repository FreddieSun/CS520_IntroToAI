from mazeCreator import createMaze, drawmaze
import numpy as np
import sys
import time
from PIL import Image

sys.setrecursionlimit(150000)


# create a parent class, for finding the minimum path
class Parent:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def bfsmaze(maze):
    n = len(maze)
    # mark whether a node is visited
    color = np.zeros([n, n])
    path = []
    for i in range(n):
        path += [[]]
        for j in range(n):
            # create a n*n two dimensional array, store each node's parent node
            path[i] += [Parent()]
    # the coordinate of the node
    x = [0]
    y = [0]
    # the beginning of the queue
    front = 0
    # the end of the queue
    end = 1
    color[0][0] = 1
    # go left,go down,go up,go right
    next = [[-1, 0], [0, 1], [0, -1], [1, 0]]

    # start counting time
    start = time.time()

    while (front < end):
        for i in range(4):
            # bfs the node at the beginning of the queue
            x_next = x[front] + next[i][0]
            y_next = y[front] + next[i][1]
            # check if the next-visit-node is in the maze and can be visited
            if 0 <= x_next <= n - 1 and 0 <= y_next <= n - 1 \
                    and color[x_next][y_next] == 0 and maze[x_next][y_next] == 0:
                # mark the node as visited
                color[x_next][y_next] = 1
                # append the end
                end += 1
                # add the qualified node in the queue
                x.append(x_next)
                y.append(y_next)
                # in the path array, mark the node's parent node.
                path[x_next][y_next].x = x[front]
                path[x_next][y_next].y = y[front]

        # start to bfs the next node in the queue.
        front += 1

        # if arrive at the destination, stop bfs.
        if x_next == n - 1 and y_next == n - 1:
            x.append(x_next)
            y.append(y_next)
            break

    # stop counting time
    end = time.time()

    print('Running time is:', end - start, 's')


    # combine the x coordinate and y coordinate togther to get the final result.
    z = list(zip(x, y))
    print('Number of nodes expanded in total:', len(z))

    # if the destination has not been visited, then there's no solution.
    if (n - 1, n - 1) not in z:
        print('No path')
        sys.exit(0)

    # return the path array as the result.
    return path


pathx = []
pathy = []


# from the destination, use a recursion way to find the minimum path.
def getpath(x, y, path):
    # reach the start, path found
    if x == 0 and y == 0:
        return
    else:
        # path[x][y] is the parent of the (x,y). Use the recursion way to continue find the path
        getpath(path[x][y].x, path[x][y].y, path)
        pathx.append(path[x][y].x)
        pathy.append(path[x][y].y)


def main():


    maze = createMaze(30, 0.3)
    n = len(maze)

    # draw the maze
    mazedrown = drawmaze(maze)
    path = bfsmaze(maze)
    getpath(n - 1, n - 1, path)
    finalpath = list(zip(pathx, pathy))

    # get the final path
    finalpath.append((n - 1, n - 1))
    print('The final path is', finalpath)
    print('The length of minimum path is', len(finalpath) - 1)


    mazex = mazedrown.load()

    # draw the path
    for i in finalpath:
        mazex[i] = (134, 205, 133)
    mazedrown.show()

    # save the final result.
    mazedrown.save('maze.png')


if __name__ == "__main__":
    main()
