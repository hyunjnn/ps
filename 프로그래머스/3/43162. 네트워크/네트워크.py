from collections import deque

def bfs(graph, start, visited):
    dq = deque([start])
    visited[start] = True
    
    while dq:
        current = dq.popleft()
        for n in graph[current]:
            if not visited[n]:
                dq.append(n)
                visited[n] = True
                
                
def solution(n, computers):
    graph = [[] for _ in range(n)]
    visited = [False] * n
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)
    
    res = 0
    for k in range(n):
        if not visited[k]:
            bfs(graph, k, visited)
            res += 1
    return res