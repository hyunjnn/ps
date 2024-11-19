import heapq
import sys

N = int(input())
q = []
for _ in range(N):
    n = int(sys.stdin.readline())
    if n == 0:
        if q:
            data = heapq.heappop(q)
            print(data[0] * data[1])
        else:
            print(0)
    elif n > 0:
        heapq.heappush(q, (n, 1))
    else:
        heapq.heappush(q, (-n, -1))
      
        
        