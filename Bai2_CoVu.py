# Ý tưởng: đưa chuỗi và dạng dãy số, kí tự X ~ +1, kí tu D ~ -1
# => bài toán quy về tìm dãy con liên tiếp dài nhất mà có tổng = 0
mp = {0: 0}
res = 0
sum = 0
for i, c in enumerate(input(), 1):
    if c == 'X': sum += 1
    else: sum -= 1
    if sum not in mp:
        mp[sum] = i
    else:
        res = max(res, i - mp[sum])
print(res)