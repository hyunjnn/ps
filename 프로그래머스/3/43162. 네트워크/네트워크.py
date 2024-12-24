from collections import deque

def dfs(graph, start, visited):
    visited[start] = True
    
    for n, connected in enumerate(graph[start]):
        if connected and not visited[n]:
            dfs(graph, n, visited)
                
                
def solution(n, computers):
    visited = [False] * n
    
    res = 0
    for k in range(n):
        if not visited[k]:
            dfs(computers, k, visited)
            res += 1
    return res