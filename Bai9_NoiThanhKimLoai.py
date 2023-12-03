import queue

res = 0
Q = queue.PriorityQueue()
n = int(input())
a = list(map(int, input().split()))
for i in range(n): Q.put(a[i])
while(Q.qsize() > 1):
    tmp = Q.get() + Q.get()
    Q.put(tmp)
    res += tmp
print(res)

