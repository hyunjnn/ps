from collections import deque
    
N, M = map(int, input().split())

maze = [[0] * M for _ in range(N)]
for i in range(N):
    row = input()
    for idx, r in enumerate(row):
        maze[i][idx] = int(r)
        
# 갈 수 있는 방향(상, 하, 좌, 우)  
directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
q = deque([(0, 0)])
maze[0][0] = 1
    
while q:
    x, y = q.popleft()
    # 도착 지점에 도달한 경우
    if y == N - 1 and x == M - 1:
        break
        
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx and nx < len(maze[0]) and 0 <= ny and ny < len(maze) and maze[ny][nx] == 1:
            maze[ny][nx] = maze[y][x] + 1
            q.append((nx, ny))
              
print(maze[N - 1][M - 1])