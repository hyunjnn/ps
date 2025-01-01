from heapq import heappop, heappush

N = int(input())
lectures = []
for _ in range(N):
    start, end = map(int, input().split())
    lectures.append((start, end))
    
lectures.sort()

# 종료 시간 관리를 위한 최소힙(가장 빨리 끝나는 강의 시간을 꺼냄)
heap = [lectures[0][1]]

for start, end in lectures[1:]:
    heappush(heap, end)
    # 강의 시작 시간이 앞 강의 종료 시간보다 작다면
    if start >= heap[0]:
        heappop(heap)
        
print(len(heap))