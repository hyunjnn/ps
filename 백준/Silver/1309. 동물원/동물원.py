MOD = 9901
N = int(input())
dp = [[0]*(N+1) for _ in range(3)]
dp[0][0] = 1  # 배치하지 않거나
dp[1][0] = 1  # 1열에 배치하거나
dp[2][0] = 1  # 2열에 배치하는 경우

for i in range(1, N+1):
    dp[0][i] = dp[0][i-1] + dp[1][i-1] + dp[2][i-1]
    dp[1][i] = (dp[0][i-1]+ dp[2][i-1])%MOD
    dp[2][i] = (dp[0][i-1]+ dp[1][i-1])%MOD

print(max(dp[0][N], dp[1][N], dp[2][N])%MOD)