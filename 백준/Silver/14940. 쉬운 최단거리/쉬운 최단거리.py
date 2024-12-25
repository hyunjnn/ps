from collections import deque

# 세로의 크기, 가로의 크기
n, m = map(int, input().split())

# 지도 정보 입력
maps = [list(map(int, input().split())) for _ in range(n)]

start_x = start_y = -1
# 시작 지점 찾기
for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            start_x, start_y = i, j
            break
    if start_x != -1:
        break

def bfs(start, end, graph):
    # 각 지점까지의 거리 정보를 저장할 배열
    distances = [[-1] * m for _ in range(n)]
    
    distances[start][end] = 0
    dq = deque([(start, end)])
    
    while dq:
        cx, cy = dq.popleft()
        # 이동 가능 방향(상, 하, 좌, 우) 탐색
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = cx + dx, cy + dy
            # 지도 범위를 벗어나지 않고
            if 0 <= nx < n and 0 <= ny < m:
                # 방문하지 않은 땅이면
                if distances[nx][ny] == -1 and graph[nx][ny] == 1:
                    # 거리 저장 및 큐에 추가
                    distances[nx][ny] = distances[cx][cy] + 1
                    dq.append((nx, ny))
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                distances[i][j] = 0
    
    return distances
    
        
# 거리 계산
dist = bfs(start_x, start_y, maps)

# 거리 출력
for row in dist:
    print(" ".join(map(str, row)))