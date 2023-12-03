from queue import Queue

n, k, m = map(int, input().split())
a = list(map(int, input().split()))
Q = Queue()
res = 0
for i in range(1, n + k):
    if i <= n: Q.put((a[i-1], i))
    tmp = m
    while Q.qsize() > 0 and tmp > 0:
        value, pos = Q.queue[0]
        if i - pos < k:
            tmp1 = min(value, tmp)
            res += tmp1
            tmp -= tmp1
            if (value <= tmp1): Q.get()
            else: Q.queue[0] = (value - tmp1, pos)
        else: Q.get()
print(res)