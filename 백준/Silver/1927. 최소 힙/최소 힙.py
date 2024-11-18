import heapq
import sys
N = int(input())
q = []
for i in range(N):
    # n = int(input())
    n = int(sys.stdin.readline())
    if n == 0:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, n)
    