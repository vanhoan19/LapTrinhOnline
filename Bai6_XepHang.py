import queue
S = queue.LifoQueue()
S.put([2e9, 0])
n = int(input())
A = list(map(int, input().split()))
res = 0
for x in A :
    while S.queue[-1][0] < x :
        res += S.queue[-1][1]
        S.get()
    if S.queue[-1][0] == x :
        res += S.queue[-1][1] + (S.queue[-2][1] != 0)
        S.queue[-1][1] += 1
    else :
        res += (S.queue[-1][1] != 0 )
        S.put([x, 1])
print(res)