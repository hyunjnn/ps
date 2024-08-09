from sys import stdin

n, m = map(int, input().split())
arr = list(map(int, stdin.readline().split()))

arr.sort()

start = 0
end = arr[-1]

res = 0
while start <= end:
    mid = (start + end) // 2
    hap = 0
    for x in arr:
        if x > mid:
            hap += x - mid
    # 가져갈 나무의 양이 부족한 경우 더 잘라야 함(= 절단기 높이 down)
    if hap < m:
        end = mid - 1
    # 가져갈 나무의 양이 충분한 경우(= 절단기 높이 up)
    else:
        start = mid + 1
        res = mid  # 최대한 덜 잘라야 하므로 기록해 둠

print(res)