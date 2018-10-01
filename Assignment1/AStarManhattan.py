from mazeCreator import createMaze
from queue import PriorityQueue as PQueue


def AStarEuclidean(x, y, maze):
    pq = PQueue()
    pq.put()




def heuristics(x,y,maze):
    N=len(maze)
    return abs(pow(N-1-x,2)+pow(N-1-y),2)



def main():
    # Generate the maze with size N*N and p
    maze = createMaze(5, 0.1)
    print(maze)


if __name__ == "__main__":
    main()
