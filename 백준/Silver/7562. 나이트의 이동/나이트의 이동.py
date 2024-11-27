from collections import deque

def bfs(graph, sx, sy, ex, ey, visited):
    # 이동 가능 방향
    directions = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    # 시작 지점 좌표, 이동 횟수 저장
    dq = deque([(sx, sy, 0)])
    visited[sx][sy] = True
    
    while dq:
        cx, cy, count = dq.popleft()
        # 목표 지점에 도달한 경우, 이동 횟수 반환
        if cx == ex and cy == ey:
            return count
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if not visited[nx][ny]:
                    dq.append((nx, ny, count + 1))
                    visited[nx][ny] = True
    
    
T = int(input())
for _ in range(T):
    
    # 체스판 한 변의 길이
    N = int(input())
    # 시작 지점
    start_x, start_y = map(int, input().split())
    # 목표 지점
    end_x, end_y = map(int, input().split())
    
    # 방문 리스트, 체스판 초기화
    visited = [[False] * N for _ in range(N)]
    graph = [[i for i in range(N)] for _ in range(N)]
    
    # 이동 횟수 계산
    print(bfs(graph, start_x, start_y, end_x, end_y, visited))