import numpy as np
from queue import PriorityQueue as PQueue


a = np.array([[1,2,3],[4,5,6]])

pq = PQueue()

pq.put((12,'十二'))
pq.put((13,'十三'))
pq.put((14,'十四'))
pq.put((1,'一'))

print(pq.qsize())

for i in range(pq.qsize()):
    print(pq[i])