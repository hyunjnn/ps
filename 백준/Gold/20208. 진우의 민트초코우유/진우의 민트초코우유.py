import sys
input = sys.stdin.readline
max_val = -sys.maxsize

N, M, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

start_x = start_y = 0  
milks = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            start_x, start_y = i, j
        elif board[i][j] == 2:
            milks.append((i, j))

def backtrack(cx, cy, total, hp):
    global max_val
    
    for mx, my in milks:
        if board[mx][my] == 2:
            dist = abs(cx-mx) + abs(cy-my)
            if dist <= hp:
                board[mx][my] = 0
                backtrack(mx, my, total+1, hp-dist+H)
                board[mx][my] = 2
            
    return_cost = abs(cx-start_x) + abs(cy-start_y)
    if return_cost <= hp:
        max_val = max(max_val, total)
                
                
backtrack(start_x, start_y, 0, M)            
print(max_val)