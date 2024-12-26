from collections import deque

N, M = map(int, input().split())
maps = [list(map(int, input())) for _ in range(N)]

def bfs(graph):
    # 이동 가능 방향(상, 하, 좌, 우)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    
    # 좌표, 이동 거리, 벽 제거 여부 
    dq = deque([(0, 0, 1, 0)])
    visited[0][0][0] = 1
    
    while dq:
        x, y, dist, broken = dq.popleft()
        # 도착한 경우 거리 반환
        if x == N-1 and y == M-1:
            return dist
        # 이동 가능 방향 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 지도 내에 위치하면서
            if 0 <= nx < N and 0 <= ny < M:
                # 방문하지 않았고, 벽이 아닌 경우
                if not visited[nx][ny][broken] and graph[nx][ny] == 0:
                    dq.append((nx, ny, dist + 1, broken))
                    visited[nx][ny][broken] = 1
                # 방문하지 않았고, 벽이지만 한번도 부순 적 없는 경우
                if visited[nx][ny][1] == 0 and graph[nx][ny] == 1 and broken == 0:
                    dq.append((nx, ny, dist + 1, 1))
                    visited[nx][ny][1] = 1
    # 목적지에 갈 수 없는 경우
    return -1 


print(bfs(maps))