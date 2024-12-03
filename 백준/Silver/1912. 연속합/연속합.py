import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().strip().split()))

dp = [0] * 100001
dp[0] = nums[0]
res = dp[0]
for i in range(1, n):
    dp[i] = max(nums[i], dp[i-1] + nums[i])
    res = max(res, dp[i])
print(res)