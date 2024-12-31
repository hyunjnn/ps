from heapq import heappush, heappop

n = int(input())
max_heap = []
for _ in range(n):
    cnt, *gifts = map(int, input().split())
    if cnt == 0:
        if max_heap:
            print(-heappop(max_heap))
        else:
            print(-1)
    else:
        for g in gifts:
            heappush(max_heap, -g)