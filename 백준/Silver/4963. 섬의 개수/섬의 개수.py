from collections import deque

def bfs(graph, x, y, visited):
    # 이동 가능 방향(상, 하, 좌, 우, 대각선)
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    
    # 방문 처리
    dq = deque([(x, y)])
    visited[x][y] = True
    
    while dq:
        x, y = dq.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    dq.append((nx, ny))
                    visited[nx][ny] = True
    
    
while True:
    # 지도의 너비, 높이
    w, h = map(int, input().split())
    # 종료 조건
    if w == 0 and h == 0:
        break
    # 방문 리스트, 지도 초기화(1: 땅, 0: 바다)
    visited = [[False for _ in range(w)] for _ in range(h)]
    graph = [list(map(int, input().split())) for _ in range(h)]
    
    # 섬의 개수 계산
    count = 0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j] == 1:
                bfs(graph, i, j, visited)
                count += 1
    print(count)