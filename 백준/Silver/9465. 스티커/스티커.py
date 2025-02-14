import sys
data = sys.stdin.read().splitlines()
line = 1
for i in range(int(data[0])):
    N = int(data[line])
    board = [list(map(int, data[line+i].split())) for i in range(1,3)]
    
    dp = [[0]*N for _ in range(3)]
    dp[1][0] = board[0][0]
    dp[2][0] = board[1][0]
    for i in range(1, N):
        dp[0][i] = max(dp[0][i-1], dp[1][i-1], dp[2][i-1])
        dp[1][i] = max(dp[0][i-1], dp[2][i-1]) + board[0][i]
        dp[2][i] = max(dp[0][i-1], dp[1][i-1]) + board[1][i]
    print(max(dp[0][N-1], dp[1][N-1], dp[2][N-1]))
    line += 3