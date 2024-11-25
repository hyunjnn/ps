from collections import deque

N = int(input())  # 컴퓨터 수
M = int(input())  # 직접 연결되어 있는 컴퓨터 쌍의 수

def bfs(graph, v, visited):
    dq = deque([v])
    visited[v] = True
    count = 0  # 감염된 컴퓨터 수
    while dq:
        q = dq.popleft()
        for node in graph[q]:
            if not visited[node]:
                visited[node] = True
                dq.append(node)
                count += 1
    return count
    
    
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(graph, 1, visited))