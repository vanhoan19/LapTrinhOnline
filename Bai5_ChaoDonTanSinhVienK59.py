import queue

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    L = [0] * n
    SL = queue.LifoQueue()
    SL.put((-1, 2e9))
    for i in range(n):
        while SL.queue[-1][1] <= a[i]: SL.get()
        L[i] = SL.queue[-1][0]
        SL.put((i, a[i]))

    R = [0] * n
    SR = queue.LifoQueue()
    SR.put((-1, 2e9))
    for i in range(n - 1, -1, -1):
        while SR.queue[-1][1] <= a[i]: SR.get()
        R[i] = SR.queue[-1][0]
        SR.put((i, a[i]))
    for i in range(n):
        if L[i] == -1 or R[i] == -1:
            print(1 + L[i] + R[i], end=" ")
        else:
            print(L[i] if i - L[i] <= R[i] - i else R[i], end=" ")
