from collections import deque

# 정점 개수, 간선 개수, 탐색 시작 번호
N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = True


visited1 = [False] * (N + 1)


def dfs(V):
    visited1[V] = True
    print(V, end=' ')
    for i in range(1, N + 1):
        if not visited1[i] and graph[V][i]:
            dfs(i)


def bfs(V):
    q = deque([V])
    visited = [False] * (N + 1)
    visited[V] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in range(1, N + 1):
            if not visited[i] and graph[v][i]:
                visited[i] = True
                q.append(i)

# dfs 수행 결과 출력
dfs(V)
print()
# bfs 수행 결과 출력
bfs(V)