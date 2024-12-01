N, M = map(int, input().split())
nums = list(map(int, input().split()))

# 누적합 계산
prefix = [0] * N
prefix[0] = nums[0]
for i in range(1, N):
    prefix[i] = prefix[i - 1] + nums[i]
    
for _ in range(M):
    a, b = map(int, input().split())
    if a == b:
        print(nums[a - 1])
        continue
    # 누적합으로 구간합 계산
    print(prefix[b - 1] - (prefix[a - 2] if a > 1 else 0))