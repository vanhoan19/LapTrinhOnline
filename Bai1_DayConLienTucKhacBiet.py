pos = {}
res = 1
st = 0
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] in pos and pos[a[i]] >= st:
        st = pos[a[i]] + 1
    res = max(res, i - st + 1)
    pos[a[i]] = i
print(res)
