import sys
data = sys.stdin.read().splitlines()
POWER = 100

N = int(data[0])
L = list(map(int, data[1].split()))
J = list(map(int, data[2].split()))
# i번째 사람까지 고려하고, 총 체력이 p일 때, 느끼는 최대 기쁨
dp = [[0]*(POWER+1) for _ in range(N+1)]

for i in range(1, N+1):
    for p in range(POWER+1):
        if p >= L[i-1]:
            dp[i][p] = max(dp[i-1][p], dp[i-1][p-L[i-1]]+J[i-1])
        else:
            dp[i][p] = dp[i-1][p]
print(dp[N][POWER-1])