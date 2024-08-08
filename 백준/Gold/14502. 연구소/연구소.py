# 지도의 세로 크기, 가로 크기
N, M, = map(int, input().split())
graph = []
temp = [[0] * M for _ in range(N)]
for i in range(N):
    arr = list(map(int, input().split()))
    graph.append(arr)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

res = 0


# 안전 영역(0인 부분) 계산
def get_score():
    score = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                score += 1
    return score


# dfs 이용해 바이러스 전파 구현
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)


# dfs 이용해 벽 설치할 때마다 안전 영역 크기 계산
def dfs(count):
    global res
    if count == 3:
        for i in range(N):
            for j in range(M):
                temp[i][j] = graph[i][j]
        for i in range(N):
            for j in range(M):
                if temp[i][j] == 2:
                    virus(i, j)
        res = max(res, get_score())
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                graph[i][j] = 0
                count -= 1


dfs(0)
print(res)
