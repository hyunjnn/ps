T = int(input())
for _ in range(T):
    n = int(input())
    dp = [(0, 0)] * (n + 1)
    dp[0] = (1, 0)
    for i in range(1, n + 1):
        dp[i] = (sum(dp[i-1]) - dp[i-1][0], sum(dp[i-1]))
    print(" ".join(map(str, dp[n])))