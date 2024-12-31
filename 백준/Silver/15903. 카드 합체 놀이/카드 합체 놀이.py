from heapq import heappush, heappop, heapify

n, m = map(int, input().split())
heap = list(map(int, input().split()))
heapify(heap)

for _ in range(m):
    data = heappop(heap) + heappop(heap)
    heappush(heap, data)
    heappush(heap, data)
print(sum(heap))