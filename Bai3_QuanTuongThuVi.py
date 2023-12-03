import collections
ans, arr1, arr2 = 0, [], []
for i in range(int(input())):
    x, y = map(int, input().split())
    arr1.append(x - y)
    arr2.append(x + y)
for x in collections.Counter(arr1).values(): ans += x * (x - 1) // 2
for x in collections.Counter(arr2).values(): ans += x * (x - 1) // 2
print(ans)
