import sys
input = sys.stdin.readline
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

R, C, K = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

visited = [[False] * C for _ in range(R)]

obstacle = []
for i in range(R):
    for j in range(C):
        if board[i][j] == "T":
            obstacle.append((i, j))
            

def backtrack(cx, cy, level):
    global count
    
    if cx == 0 and cy == C - 1 and level == K:
        count += 1
        return
    
    for dx, dy in DIRECTIONS:
        nx, ny = dx + cx, dy + cy
        if 0<=nx<R and 0<=ny<C and not visited[nx][ny]:
            if board[nx][ny] == "T": continue
            visited[nx][ny] = True
            backtrack(nx, ny, level+1)
            visited[nx][ny] = False
    

count = 0
visited[R-1][0] = True
backtrack(R-1, 0, 1)
print(count)