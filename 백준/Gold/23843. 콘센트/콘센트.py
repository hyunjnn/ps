import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m = map(int, input().split())
charging_time = list(map(int, input().split()))

min_heap = []
for t in sorted(charging_time, reverse=True):
    # 콘센트가 비어있으면 꽂고
    if len(min_heap) < m:
        heappush(min_heap, t)
    # 없으면 먼저 끝나는 거 빼서 꽂음
    else:
        outcome = heappop(min_heap)
        heappush(min_heap, outcome + t)

print(max(min_heap))
