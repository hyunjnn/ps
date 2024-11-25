from collections import deque
  
N = int(input())  # 지도의 크기
visited = [[False] * N for _ in range(N)]
graph = [[] for _ in range(N)]

# 지도 설정
for i in range(N):
    row = input()
    for r in row:
        graph[i].append(int(r))
        
def bfs(graph, x, y, visited):
    # 이동 방향(상, 하, 좌, 우)
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    count = 1  # 단지내 집의 수
    dq = deque([(x, y)])
    visited[x][y] = True  # 방문 처리
    
    while dq:
        cx, cy = dq.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(graph) and 0 <= ny < len(graph):
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    count += 1
                    dq.append((nx, ny))
    return count
    
        
count = 0  # 총 단지수
counts = []  # 각 단지내 집의 수
for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == 1:
            count += 1
            counts.append(bfs(graph, i, j, visited))
            
print(count)
for c in sorted(counts):
    print(c)