import sys
imput = sys.stdin.readline

N, K = map(int, input().split())
C = map(int, input().split())

# 카페인 양이 k가 되기 위한 최소 커피 개수
dp = [1e9]*(K+1)
dp[0] = 0

for c in C:
    for i in range(K, c-1, -1):
        dp[i] = min(dp[i], dp[i-c]+1)
        
print(dp[K] if dp[K] != 1e9 else -1)