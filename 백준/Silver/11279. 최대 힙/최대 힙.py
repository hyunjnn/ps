import heapq
import sys

N = int(input())
q = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if n == 0:
        if q:
            print(-heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q, -n)