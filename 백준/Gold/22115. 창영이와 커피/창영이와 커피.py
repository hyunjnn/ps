import sys
imput = sys.stdin.readline

N, K = map(int, input().split())
C = list(map(int, input().split()))
# i번 커피까지 확인했을 때, 카페인 양이 k가 되기 위한 최소 커피 개수
dp = [[1e9]*(K+1) for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = 0

for i in range(1, N+1):
    for c in range(K+1):
        if c < C[i-1]:
            dp[i][c] = dp[i-1][c]
        else:
            dp[i][c] = min(dp[i-1][c], dp[i-1][c-C[i-1]] + 1)
        
print(dp[N][K] if dp[N][K] != 1e9 else -1)