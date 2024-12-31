import sys
from heapq import heappush, heappop
input = sys.stdin.readline

# 보석과 가방의 개수 입력
N, K = map(int, input().split())

# 보석의 무게와 가격 입력 
jewels = [tuple(map(int, input().strip().split())) for _ in range(N)]
jewels.sort()

# 가방의 최대 무게 입력
bags = [int(input()) for _ in range(K)]
bags.sort()

money = 0  
max_heap = []
i = 0
# 용량이 작은 가방부터 
for bag in bags:
    # 가방에 들어가는 보석의 가격을 최대힙에 추가          
    while i < N and jewels[i][0] <= bag:
        heappush(max_heap, -jewels[i][1])
        i += 1
    if max_heap:
        # 가방에 넣을 수 있는 보석 중 가장 비싼 보석의 금액을 더함
        money += -heappop(max_heap)

print(money)    