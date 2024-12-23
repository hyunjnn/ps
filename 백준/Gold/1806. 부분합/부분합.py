import sys

N, S = map(int, input().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

end = 0
# 최소 길이를 저장할 변수
res = int(1e9)
sub_sum = 0

for start in range(N):
    while sub_sum < S and end < N:
        sub_sum += arr[end]
        end += 1
    if sub_sum >= S:
        res = min(res, end - start)
    sub_sum -= arr[start]

print(res if res != int(1e9) else 0)