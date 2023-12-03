import collections
import queue
PQ = queue.PriorityQueue()
res = 0
for x in collections.Counter(input()).values(): PQ.put(x)
while(PQ.qsize() > 1):
    tmp = PQ.get() + PQ.get()
    res += tmp
    PQ.put(tmp)
print(res)