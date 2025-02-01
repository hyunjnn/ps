import sys
from bisect import bisect_left

data = sys.stdin.read().splitlines()
line = 0

while line < len(data):
    n = data[line]
    nums = list(map(int, data[line+1].split()))
    res = []
    for n in nums:
        position = bisect_left(res, n)
        if position == len(res):
            res.append(n)
        else:
            res[position] = n
    print(len(res))
    line += 2