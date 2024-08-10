from sys import stdin

n, c = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(stdin.readline().rstrip()))

arr.sort()
start = 1
end = arr[-1] - arr[0]

gap = 0
while start <= end:
    mid = (start + end) // 2  # 공유기 사이의 거리
    cnt = 1  # 설치한 공유기 개수
    x = arr[0]  # 첫 번째 공유기 설치 위치
    for i in range(1, n):
        if arr[i] >= x + mid:  # 공유기 설치 과정
            cnt += 1
            x = arr[i]
    if cnt >= c:
        start = mid + 1
        gap = mid  # 가장 인접한 두 공유기 사이의 최대 거리를 구하기 위한 기록
    else:
        end = mid - 1
print(gap)
