import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def get_kevin(start):
    dist = [0] + [-1]*N
    dist[start] = 0
    q = deque([start])
    while q:
        now = q.popleft()
        for nxt in graph[now]:
            if dist[nxt] == -1:
                dist[nxt] = dist[now]+1
                q.append(nxt)
    return sum(dist)
        
min_val = 1e9
res = 1
for user in range(1, N+1):
    kevin = get_kevin(user)
    if kevin < min_val:
        min_val = kevin
        res = user
print(res)