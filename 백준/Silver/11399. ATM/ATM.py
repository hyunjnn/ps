import sys
input = sys.stdin.readline

N = int(input())
times = sorted(map(int, input().split()))
dp = [0]*(N)
dp[0] = times[0]
for i in range(1, N):
    dp[i] = dp[i-1] + times[i]
print(sum(dp))