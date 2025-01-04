from heapq import heappop, heappush

N = int(input())
heap = []
for _ in range(N):
    heappush(heap, int(input()))
    
while len(heap) > 1:
    a, b = heappop(heap), heappop(heap)
    heappush(heap, (a + b) / 2)
print(heappop(heap))