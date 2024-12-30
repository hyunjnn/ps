from collections import deque

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
# 익은 토마토 찾기
queue = deque([(i, j) for i in range(N) for j in range(M)if box[i][j] == 1])

def bfs():
    # 익지 않은 토마토가 없는 경우
    if all(0 not in row for row in box):
        return 0
    days = 0
    while queue:
        # 큐에는 하루동안 관찰할 토마토가 들어있음
        for _ in range(len(queue)):
            x, y = queue.popleft()
            # 상, 하, 좌, 우 토마토 주변 탐색
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                # 익지 않은 토마토라면
                if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                    # 익은 토마토가 됨
                    box[nx][ny] = 1
                    queue.append((nx, ny))
        # 하루가 지남
        days += 1
        
    return -1 if any(0 in row for row in box) else days - 1
            
    
print(bfs())