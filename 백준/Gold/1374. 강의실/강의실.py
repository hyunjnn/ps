from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())

lectures = []
for _ in range(N):
    lec_num, *data = map(int, input().split())
    lectures.append((data[0], data[1]))
    
lectures.sort()

heap = []
heappush(heap, lectures[0][1])

for start, end in lectures[1:]:
    heappush(heap, end)
    if start >= heap[0]:
        heappop(heap)
        
print(len(heap))