import sys
from bisect import bisect_left

data = sys.stdin.read().splitlines()
line = 1
for test in range(int(data[0])):
    N, K = map(int, data[line].split())
    nums = list(map(int, data[line+1].split()))
    lis = []
    is_k_len = False
    for n in nums:
        pos = bisect_left(lis, n)
        if pos == len(lis):
            lis.append(n)
        else:
            lis[pos] = n
        if len(lis) == K:
            is_k_len = True
    print(f"Case #{test+1}")
    print(1) if is_k_len else print(0)
    line += 2