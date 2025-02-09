import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
q = int(input())

# i부터 j까지의 수가 팰린드롬이면 1, 아니면 0
dp = [[0]*N for _ in range(N)]
# 길이 1
for i in range(N): 
    dp[i][i] = 1
# 길이 2  
for i in range(N - 1):
    dp[i][i+1] = 1 if nums[i] == nums[i+1] else 0
# 길이 3 ~ N
for l in range(3, N+1):
    for i in range(N-l+1):
        j = i+l-1
        if nums[i] == nums[j] and dp[i+1][j-1]:
            dp[i][j] = 1

for _ in range(q):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])