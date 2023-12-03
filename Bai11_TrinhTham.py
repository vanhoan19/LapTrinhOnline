import  queue

Q = queue.PriorityQueue()
n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    Q.put([-a[i], i])
    if (i >= k-1):
        while(i - Q.queue[0][1] >= k):
            Q.get()
        print(-Q.queue[0][0], end=" ")
