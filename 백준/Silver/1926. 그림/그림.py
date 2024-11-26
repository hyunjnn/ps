from collections import deque

def bfs(graph, x, y, visited):
    # 색칠된 그림 넓이
    count = 1 
    # 이동 가능 방향(상, 하, 좌, 우)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # 방문 처리
    dq = deque([(x, y)])
    visited[x][y] = True
    
    # 색칠된 그림 넓이 계산 
    while dq:
        x, y = dq.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    dq.append((nx, ny))
                    count += 1
    return count


# 도화지의 세로, 가로 길이
n, m = map(int, input().split())
# 도화지 초기화(0: 색칠X, 1: 색칠O)
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

count = 0  # 총 그림의 개수
max_val = 0  # 가장 넓은 그림의 넓이
for i in range(n):
    for j in range(m):
        if not visited[i][j] and paper[i][j] == 1:
            count += 1
            max_val = max(max_val, bfs(paper, i, j, visited))
            
print(count)
print(max_val)