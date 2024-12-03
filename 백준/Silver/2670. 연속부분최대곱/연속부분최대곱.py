N = int(input())
nums = [float(input()) for _ in range(N)]

dp = [0] * 10001
dp[0] = nums[0]
# 최댓값을 저장할 변수
res = dp[0]
for i in range(1, N):
    dp[i] = max(nums[i], dp[i-1] * nums[i])
    res = max(res, dp[i])
# 연속된 수들의 곱의 최댓값 출력
print(f"{res:.3f}")