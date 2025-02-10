import sys
input = sys.stdin.readline

N, T = map(int, input().split())
data = []
for _ in range(N):
    # 공부 시간, 배점
    K, S = map(int, input().split())
    data.append((K, S))
    
# i 단원, j 시간에 얻는 최대 점수    
dp = [[0]*(T+1) for _ in range(N+1)]    

for i in range(1, N+1):
    for t in range(T+1):
        time, score = data[i-1]
        if time > t:
            dp[i][t] = dp[i-1][t]
        else:
            dp[i][t] = max(dp[i-1][t], dp[i-1][t-time]+score)

print(dp[N][T])