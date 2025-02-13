N, M = map(int, input().split())
items = []
for _ in range(M):
    days, pages = map(int, input().split())
    items.append((days, pages))
dp = [[0]*(N+1) for _ in range(M+1)]
for i in range(1, M+1):  # 챕터
    day, page = items[i-1]
    for j in range(1, N+1):  # 날짜
        if j < day:  # 기간 내에 못 읽거나
            dp[i][j] = dp[i-1][j]
        else:  # 읽거나
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-day]+page)
print(dp[M][N])