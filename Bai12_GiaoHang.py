from queue import PriorityQueue
A =[[] for i in range(1005)]
n = int(input())
for i in range(n):
    t, v = map(int, input().split())
    A[t].append(v)
Q = PriorityQueue()
res = 0
for i in range(1000,0,-1):
    for x in A[i]: Q.put(-x)
    if Q.qsize():
        res+=Q.get()
print(-res)