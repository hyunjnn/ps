from heapq import heappop, heappush

# 버스의 개수
N = int(input())

scheduled = []
for _ in range(N):
    start, end = input().split()
    
    scheduled.append((int(start.replace(":", "").replace(".", "")), int(end.replace(":", "").replace(".", ""))))
    
scheduled.sort()

min_heap = [scheduled[0][1]]
for start, end in scheduled[1:]:
    if start >= min_heap[0]:
        heappop(min_heap)
    heappush(min_heap, end)
print(len(min_heap))