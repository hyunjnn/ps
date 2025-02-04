from bisect import bisect_left
import sys

data = sys.stdin.read().splitlines()
line = 1

for _ in range(int(data[0])):
    N = int(data[line])
    
    line += 1
    nums = map(int, data[line:line+N])
    lis = []
    for n in nums:
        pos = bisect_left(lis, n)
        if pos == len(lis):
            lis.append(n)
        else:
            lis[pos] = n
    print(len(lis))
    line += N
        