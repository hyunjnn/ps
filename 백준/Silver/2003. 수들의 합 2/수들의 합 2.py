import sys

N, M = map(int, input().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

end = 0
count = 0
current_sum = 0
for start in range(N):
    while current_sum < M and end < N:
        current_sum += arr[end]
        end += 1
    if current_sum == M:
        count += 1
    current_sum -= arr[start]

print(count)