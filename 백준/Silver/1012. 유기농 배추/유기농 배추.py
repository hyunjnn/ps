from collections import deque

def bfs(x, y, graph, visited):
    # 갈 수 있는 방향(상, 하, 좌, 우)
    directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]
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
    # 가로, 세로 길이, 배추 위치 개수
    M, N, K = map(int, input().split())
    # 배추 밭 초기화
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    # 배추 표시
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1
    # 필요한 지렁이 계산
    worm = 0
    for y in range(N):
        for x in range(M):
            if graph[y][x] == 1 and not visited[y][x]:
                bfs(x, y, graph, visited)
                worm += 1
    print(worm)
    
    