from collections import deque

def bfs(graph, x, y, visited, h):
    # 이동 가능 방향(상, 하, 좌, 우)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # 방문 처리
    dq = deque([(x, y)])
    visited[x][y] = True
    
    # 물에 잠기지 않는 안전 영역 방문 처리
    while dq:
        x, y = dq.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if not visited[nx][ny] and graph[nx][ny] > h: 
                    visited[nx][ny] = True
                    dq.append((nx, ny))
    

# 행과 열의 개수
N = int(input())
# 지역 높이 정보 초기화
graph = [list(map(int, input().split())) for _ in range(N)]


res = [1]
# 물에 잠기지 않는 안전 영역 계산
for h in range(1, 101):
    count  = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] > h:
                count += 1
                bfs(graph, i, j, visited, h)
    res.append(count)
print(max(res))