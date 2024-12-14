n, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
res = 0
for m in arr[::-1]:
    if m <= k:
        res += k // m
        k -= (k // m) * m
print(res)        