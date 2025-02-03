import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

nums.reverse()

res = []
for n in nums:
    pos = bisect_left(res, n)
    if pos == len(res):
        res.append(n)
    else:
        res[pos] = n
print(len(res))