import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = []
for _ in range(N):
    w, v = map(int, input().split())
    items.append((w, v))
    
# i번째 아이템까지 고려하고, 배낭 용량이 j일 때 얻는 최대 가치 
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    weight, value = items[i-1]
    for w in range(K + 1):
        if weight > w:
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight]+value)
print(dp[N][K])    