import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
DIRECTIONS = [(0, 1), (1,0), (-1,0), (0,-1)]

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1]*N for _ in range(M)]

def dfs(x, y):
    if x==M-1 and y==N-1:  # 오른쪽 하단 도착 
        return 1
    if dp[x][y] != -1:  # 메모이제이션
        return dp[x][y]
    dp[x][y] = 0  # 방문 처리
    for dx, dy in DIRECTIONS:
        nx, ny = x+dx, y+dy
        if 0<=nx<M and 0<=ny<N: 
            if board[nx][ny]<board[x][y]:  # 내리막
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]      
  # 왼쪽 상단에서 출발
print(dfs(0, 0))