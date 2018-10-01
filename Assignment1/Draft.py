import numpy as np
from queue import PriorityQueue as PQueue


a = np.array([[1,2,3],[4,5,6]])

pq = PQueue()

pq.put(12,'12')
pq.put(13,'13')
pq.put(14,'14')
pq.put(1,'1')

print(pq.queue)

print(pq.get(0))
print(pq.get(0))


