from bisect import bisect_left
N = int(input())
A = list(map(int, input().split()))

res = []
for a in A:
    pos = bisect_left(res, a)
    if pos == len(res):
        res.append(a)
    else:
        res[pos] = a
print(len(res))    