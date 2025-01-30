import sys
input = sys.stdin.readline
DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
max_val = -sys.maxsize

def backtrack(count, x, y, total):
    if count == K:
        global max_val
        max_val = max(max_val, total)
        return
    
    for i in range(x, N):
        for j in range(y if i==x else 0, M):
            if visited[i][j]: 
                continue
            neighbor_selected = False
            for dx, dy in DIRECTIONS:
                nx, ny = dx + i, dy + j
                if 0<=nx<N and 0<=ny<M and visited[nx][ny]:
                    neighbor_selected = True
            if neighbor_selected:
                continue
            visited[i][j] = True
            backtrack(count+1, i, j, total+board[i][j])
            visited[i][j] = False

N, M, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

backtrack(0, 0, 0, 0)
print(max_val)    