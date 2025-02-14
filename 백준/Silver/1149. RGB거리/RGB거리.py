import sys
input = sys.stdin.readline

N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]
dp = costs[0][:]
for i in range(1, N):
    new_dp = []
    new_dp.append(min(dp[1], dp[2]) + costs[i][0])
    new_dp.append(min(dp[0], dp[2]) + costs[i][1])
    new_dp.append(min(dp[1], dp[0]) + costs[i][2])
    dp = new_dp
print(min(dp))