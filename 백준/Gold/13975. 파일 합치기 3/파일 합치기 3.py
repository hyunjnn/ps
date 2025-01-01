import sys
from heapq import heappush, heappop, heapify
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    
    K = int(input())
    files = list(map(int, input().split()))
    heapify(files)
    
    min_val = 0
    while len(files) > 1:
        new_cost = heappop(files) + heappop(files)
        heappush(files, new_cost)
        min_val += new_cost

    print(min_val)