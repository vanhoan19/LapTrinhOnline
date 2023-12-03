from queue import LifoQueue
def Search(n, S):
    S.put(n)
    res = {n}
    while S.qsize()>0:
        u = S.get()
        m = int(u**0.5)
        for a in range(1, m+1):
            if u%a==0:
                v = (a-1)*(u//a+1)
                if v not in res:
                    S.put(v)
                    res.add(v)
    return res

if __name__ == '__main__':
    n = int(input())
    S = LifoQueue()
    print(*Search(n, S))
