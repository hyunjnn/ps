from collections import deque

def bfs(x, y, graph, visited):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = deque([(x, y)])
    visited[y][x] = True
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:       
            nx, ny = cx + dx, cy + dy
            if 0 <= nx and nx < len(graph[0]) and 0 <= ny and ny < len(graph) and not visited[ny][nx] and graph[ny][nx] == 1:
                visited[ny][nx] = True
                queue.append((nx, ny))
            
    
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    visited = [[False] * M for _ in range(N)]
    graph = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1
        
    worm = 0
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1 and not visited[y][x]:
                bfs(x, y, graph, visited)
                worm += 1
    print(worm)
        
    
    
    
    