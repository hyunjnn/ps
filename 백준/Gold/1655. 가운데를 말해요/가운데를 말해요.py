from heapq import heappush, heappop
import sys

N = int(input())
max_heap = []
min_heap = []
for _ in range(N):
    n = int(sys.stdin.readline())
    heappush(max_heap, -n)
    if min_heap and -max_heap[0] > min_heap[0]:
        heappush(min_heap, -heappop(max_heap))
    if len(max_heap) > len(min_heap) + 1:
        heappush(min_heap, -heappop(max_heap))
    elif len(max_heap) < len(min_heap):
        heappush(max_heap, -heappop(min_heap))
    print(-max_heap[0])
    