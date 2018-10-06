import numpy as np
from queue import PriorityQueue as PQueue
from Cell import *
import heapq

cells = []

A = Cell(2, 2, True)
B = Cell(2, 2, True)

heapq.heapify(cells)
heapq.heappush(cells, (10, A))
heapq.heappush(cells, (10, B))

print(heapq.heappop(cells))
print(heapq.heappop(cells))

