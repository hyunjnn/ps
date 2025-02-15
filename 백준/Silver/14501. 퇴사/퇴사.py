import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*(N+1)
for d in range(1, N+1):
    time, pay = map(int, input().split())
    dp[d] = max(dp[d], dp[d-1])
    if d+time-1 <= N:
        dp[d+time-1] = max(dp[d+time-1], dp[d-1]+pay)

print(dp[-1])    