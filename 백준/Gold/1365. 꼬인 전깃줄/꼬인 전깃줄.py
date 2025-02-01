from bisect import bisect_left

N = int(input())
nums = list(map(int, input().split()))

res = []
for n in nums:
    i = bisect_left(res, n)
    if i == len(res):
        res.append(n)
    else:
        res[i] = n
    
print(N-len(res))