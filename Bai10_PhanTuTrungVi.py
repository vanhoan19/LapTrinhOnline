import queue

L, R = queue.PriorityQueue(), queue.PriorityQueue()
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if(i%2==0): L.put(-a[i])
    else: R.put(a[i])
    if R.qsize()>0 and -L.queue[0] > R.queue[0]:
        L.put(-R.get())
        R.put(-L.get())
    print(-L.queue[0], end=" ")

