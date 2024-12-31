from heapq import heappush, heappop

N = int(input())
arr = []

# 강의 시작 시간과 끝나는 시간 입력
for _ in range(N):
    start, end = map(int, input().split())
    arr.append((start, end))
    
# 시작 시간이 빠른 순으로 정렬    
arr.sort()
# 종료 시간을 저장할 최소힙
hq = []

for start, end in arr:
    # 제일 빠른 종료 시간보다 시작 시간이 늦어야 강의실 재사용 가능
    if hq and hq[0] <= start:
        heappop(hq)
    
    heappush(hq, end)
    
# 필요한 강의실의 최소 개수 출력
print(len(hq))