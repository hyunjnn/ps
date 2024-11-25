from collections import deque

# 정점의 개수, 간선의 개수
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

# 그래프 정보 입력
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(graph, v, visited):
    dq = deque([v])
    visited[v] = True
    while dq:
        q = dq.popleft()
        for node in graph[q]:
            if not visited[node]:
                dq.append(node)
                visited[node] = True
        
res = 0        
for i in range(1, N + 1):
    if not visited[i]:
        res += 1
        bfs(graph, i, visited)    
print(res)