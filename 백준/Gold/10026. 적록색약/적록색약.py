from collections import deque

def bfs(graph, x, y, visited, is_적록색약):
    # 방문 처리
    dq = deque([(x, y)])
    visited[x][y] = True
    
    # 이동 가능 방향(상, 하, 좌, 우)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while dq:
        cx, cy = dq.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and not visited[nx][ny]:
                if is_적록색약:
                    if (graph[nx][ny] in "RG" and graph[cx][cy] in "RG") or (graph[nx][ny] == graph[cx][cy]):
                        dq.append((nx, ny))
                        visited[nx][ny] = True
                else:
                    if graph[nx][ny] == graph[cx][cy]:
                        dq.append((nx, ny))
                        visited[nx][ny] = True

# 그림의 크기(N x N)
N = int(input())
# 그림(R: 빨강, G: 초록, B: 파랑)
grid = [[color for color in input()] for _ in range(N)]
# 방문 리스트
visited1 = [[False] * N for _ in range(N)]
visited2 = [[False] * N for _ in range(N)]

is_적록색약_count = 0
is_not_적록색약_count = 0

# 적록색약인 사람이 봤을 때, 아닌 사람이 봤을 때 구역 수 계산
for is_적록색약 in [True, False]:
    for i in range(N):
        for j in range(N):
            if is_적록색약:
                if not visited1[i][j]:
                    is_적록색약_count += 1
                    bfs(grid, i, j, visited1, True)
            else:
                if not visited2[i][j]:
                    is_not_적록색약_count += 1
                    bfs(grid, i, j, visited2, False)
            
                
print(is_not_적록색약_count, is_적록색약_count)