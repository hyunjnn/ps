import sys
input = sys.stdin.readline
max_val = -sys.maxsize
DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

R, C, T = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]  

def backtrack(cx, cy, total, level):
    global max_val
    
    if level == T:
        max_val = max(max_val, total)
        return 
    
    visited[cx][cy] = True
    backtrack(cx, cy, total, level+1)
    visited[cx][cy] = False
    
    for dx, dy in DIRECTIONS:
        nx, ny = cx+dx, cy+dy
        
        if 0<=nx<R and 0<=ny<C and not visited[nx][ny]:
            if board[nx][ny] != "#":
                visited[nx][ny] = True
            
                if board[nx][ny] == "S":
                    board[nx][ny] = "."
                    backtrack(nx, ny, total+1, level+1)
                    board[nx][ny] = "S"
                else:
                    backtrack(nx, ny, total, level+1)
                
                visited[nx][ny] = False
                
                               
for x in range(R):
    for y in range(C):
        if board[x][y] == "G":
            visited[x][y] = True
            backtrack(x, y, 0, 0)  
            visited[x][y] = False
            
print(max_val)