import sys
from heapq import heappush, heappop, heapify
input = sys.stdin.read
data = input().split()

i = 1
for _ in range(int(data[0])):
    K = int(data[i])
    files = list(map(int, data[i + 1 : K + i + 1]))
    i += K + 1
    heapify(files)
    
    min_val = 0
    while len(files) > 1:
        new_cost = heappop(files) + heappop(files)
        heappush(files, new_cost)
        min_val += new_cost

    print(min_val)