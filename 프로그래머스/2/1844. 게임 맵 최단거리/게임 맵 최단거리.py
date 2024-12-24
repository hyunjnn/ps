from collections import deque

def bfs(maps, start_x, start_y, end_x, end_y):
    # 이동 가능 방향(상, 하, 좌, 우)
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    # 방문 여부
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
                  
    # 이동 거리, 시작 좌표
    dq = deque([(1, start_x, start_y)])
    visited[start_x][start_y] = True
    
    while dq:
        dist, x, y = dq.popleft()
        # 목적지 도착한 경우 최단 거리 반환
        if x == end_x and y == end_y:
            return dist 
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 게임 맵을 벗어나지 않고,
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                # 벽으로 막혀있지 않고, 방문하지 않은 경우
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    # 방문함
                    dq.append((dist + 1, nx, ny))
                    visited[nx][ny] = True
                                 
    return -1  # 도착 가능한 경로가 없는 경우                    
    

def solution(maps):
    return bfs(maps, 0, 0, len(maps) - 1, len(maps[0]) - 1)