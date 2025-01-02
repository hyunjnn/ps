from collections import deque

def bfs():
    DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    
    # 시작 좌표
    q = deque([(0, 0)])
    dist[0][0] = 0
    
    while q:
        x, y = q.popleft()
     
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            # 미로 범위 확인
            if 0 <= nx < N and 0 <= ny < M:
                # 벽이 아닌 경우
                if maps[nx][ny] == 0 and dist[nx][ny] > dist[x][y]:
                    q.appendleft((nx, ny))
                    dist[nx][ny] = dist[x][y]
                # 벽인 경우
                elif maps[nx][ny] == 1 and dist[nx][ny] > dist[x][y] + 1:
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
    # 최소 비용 반환
    return dist[N - 1][M - 1]

# 가로, 세로 길이
M, N = map(int, input().split())
maps = [list(map(int, input().strip())) for _ in range(N)]
dist = [[int(1e9)] * M for _ in range(N)]

print(bfs())