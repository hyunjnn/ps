from heapq import heappush, heappop

N = int(input())

data = []
for _ in range(N):
    deadline, noodles = map(int, input().split())
    data.append((deadline, noodles))
# 빨리 끝나는 작업 중 받는 라면의 개수가 큰 것을 선택하기 위한 정렬    
data.sort()

# 라면 개수가 가장 작은 작업을 제거하기 위한 최소힙
heap = []
for d, n in data:
    heappush(heap, (n, d))
    if len(heap) > d:
        heappop(heap)
        
print(sum(x[0] for x in heap))