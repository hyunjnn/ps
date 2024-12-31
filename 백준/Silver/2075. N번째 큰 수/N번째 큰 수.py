from heapq import heappush, heappop

N = int(input())
# 가장 큰 N개의 숫자만 관리
heap = []
for _ in range(N):
    nums = list(map(int, input().split()))
    for n in nums:
        if len(heap) < N:
            heappush(heap, n)
        elif n > heap[0]:
            heappop(heap)
            heappush(heap, n)
# N번째로 큰 값 출력    
print(heappop(heap))