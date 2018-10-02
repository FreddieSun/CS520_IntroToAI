import numpy as np
from queue import PriorityQueue as PQueue
from Cell import *
import heapq

cells=[]

A=Cell(17,2,True)
B=Cell(2,3,True)
C=Cell(3,4,False)
D=Cell(4,5,False)

heapq.heapify(cells)

heapq.heappush(cells,(4,D))
heapq.heappush(cells,(1,A))
heapq.heappush(cells,(2,B))
heapq.heappush(cells,(3,C))

print(heapq.heappop(cells)[1].x)
print(heapq.heappop(cells)[1].x)