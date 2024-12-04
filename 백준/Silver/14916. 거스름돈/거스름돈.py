n = int(input())
INF = int(1e9)
dp = [INF] * 100001
dp[0] = 0
for i in range(1, n + 1):
    for coin in [2, 5]:
        if i - coin >=0:
            dp[i] = min(dp[i], dp[i-coin] + 1)
print(dp[n]) if dp[n] != INF else print(-1)