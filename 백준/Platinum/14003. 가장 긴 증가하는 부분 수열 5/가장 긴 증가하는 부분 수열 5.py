import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

lis = []
index = [0] * N 
pre = [-1] * N
for i, n in enumerate(nums):
    pos = bisect_left(lis, n)
    if pos == len(lis):
        lis.append(n)
    else:
        lis[pos] = n
        
    index[pos] = i
    if pos > 0:
        pre[i] = index[pos-1]
        
res = []
idx = index[len(lis)-1]
while idx != -1:
    res.append(nums[idx])
    idx = pre[idx]
    
print(len(res))
print(*res[::-1])