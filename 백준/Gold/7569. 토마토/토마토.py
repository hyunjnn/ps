from collections import deque

# 토마토 상자의 가로, 세로, 높이 입력
M, N, H = map(int, input().split())
# 토마토의 익힘 정도 입력
box = [
    [list(map(int, input().split())) for _ in range(N)]
    for _ in range(H)
]
# 토마토가 익는 방향 (상, 하, 좌, 우, 위, 아래)
DIRECTIONS = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

# 익은 토마토 판별
queue = deque([
    (h, n, m)
    for h in range(H)
    for n in range(N)
    for m in range(M)
    if box[h][n][m] == 1
])

def bfs():
    if all(0 not in row for layer in box for row in layer):
        return 0
    days = 0
    while queue:
        # 큐에 들어있는 토마토는 하루동안 검사해야 함
        for _ in range(len(queue)):
            h, x, y = queue.popleft()
            # 익지 않은 토마토 찾기
            for dh, dx, dy in DIRECTIONS:
                nh, nx, ny = h + dh, x + dx, y + dy
                # 상자 안에 위치하면서 익지 않은 토마토인 경우
                if 0 <= nx < N and 0 <= ny < M and 0 <= nh < H and box[nh][nx][ny] == 0:
                    # 익음
                    box[nh][nx][ny] = 1
                    queue.append((nh, nx, ny))
        # 하루 지남          
        days += 1
                
    return -1 if any(0 in row for layer in box for row in layer) else days - 1

print(bfs())