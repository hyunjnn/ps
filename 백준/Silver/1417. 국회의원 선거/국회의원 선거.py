from heapq import heappush, heappop

N = int(input())
# 다솜이 지지자의 수
target = int(input())
max_heap = []
for _ in range(N - 1):
    heappush(max_heap, -int(input()))
res = 0    
while max_heap and target <= -max_heap[0]:
    max_val = -heappop(max_heap)
    target += 1
    heappush(max_heap, -(max_val - 1))
    res += 1
print(res)