import sys
input = sys.stdin.readline
min_val = sys.maxsize
DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def backtrack(level, total):
    if level == 3:
        global min_val
        min_val = min(min_val, total)
        return
    
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
                
            wilted = False
            cost = board[i][j]
            positions = [(i, j)]
            for dx, dy in DIRECTIONS:
                nx, ny = dx + i, dy + j
                if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                    cost += board[nx][ny]
                    positions.append((nx, ny))
                else:
                    wilted = True
                    break
                    
            if not wilted:
                for px,py in positions:
                    visited[px][py] = True
                backtrack(level+1, total+cost)
                for px, py in positions:
                    visited[px][py] = False
        

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

backtrack(0, 0)
print(min_val)