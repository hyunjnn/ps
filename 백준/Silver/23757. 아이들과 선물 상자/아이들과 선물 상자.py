from heapq import heappop, heappush, heapify
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
gifts = list(map(int, input().split()))
children = list(map(int, input().split()))

max_heap = [-g for g in gifts]
heapify(max_heap)

all_satisfied = True

for child in children:
    if -max_heap[0] < child:
        all_satisfied = False
        break
    gift = -heappop(max_heap)
    heappush(max_heap, -(gift - child))
print(1 if all_satisfied else 0)