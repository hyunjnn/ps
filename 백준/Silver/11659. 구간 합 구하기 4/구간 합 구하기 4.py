import sys

N, M = map(int, sys.stdin.readline().strip().split())
nums = list(map(int, sys.stdin.readline().strip().split()))

# 누적합 계산
prefix = [0] * N
prefix[0] = nums[0]
for i in range(1, N):
    prefix[i] = prefix[i - 1] + nums[i]
    
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    # 누적합으로 구간합 계산
    print(prefix[b - 1] - (prefix[a - 2] if a > 1 else 0))