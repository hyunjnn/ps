MOD = 1000000000

# 길이
n = int(input())

# 길이 i, 마지막 수(0-9) j인 계단 수의 개수
dp = [[0]*10 for _ in range(n+1)]

# 길이가 1이면 계단 수는 1개로 초기화
for j in range(1, 10):
    dp[1][j] = 1

for i in range(2, n+1):
    dp[i][0] = dp[i-1][1]  # 0옆에는 1만 가능
    dp[i][9] = dp[i-1][8]  # 9옆에는 8만 가능
    for j in range(1, 9):  # 그 이외는 1 작거나 1 큰 수 가능
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % MOD

# 길이가 n인 계단 수의 개수 출력    
print(sum(dp[n]) % MOD)