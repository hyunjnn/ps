# 가지고 있는 랜선 개수, 필요한 랜선 개수
K, N = map(int, input().split())
# 가지고 있는 랜선의 길이
arr = [int(input()) for _ in range(K)]
arr.sort()

start = 1
end = max(arr)
res = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    
    for a in arr:
        total += (a // mid)
    # 필요한 랜선의 개수보다 적으면 적게 자르기(왼쪽 탐색)
    if total < N:
        end = mid - 1
    else:
        res = mid
        start = mid + 1
print(res)
