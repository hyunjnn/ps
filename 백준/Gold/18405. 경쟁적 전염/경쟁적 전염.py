from collections import deque

n , k = map(int, input().split())
graph = [] # 전체 정보
data = [] # 바이러스 정보
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 있는 경우
        if graph[i][j] != 0:
            # 바이러스 정보(종류, 시간, 위치) 저장
            data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)
target_s, target_x, target_y = map(int, input().split())

# 바이러스 전파 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while q:
    virus, time, x, y = q.popleft()
    if time == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, time + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])