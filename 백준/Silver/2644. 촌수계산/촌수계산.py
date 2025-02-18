import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
def bfs(start, end):
    dist = [-1]*(n+1)
    dist[start] = 0
    q = deque([start])
    while q:
        cur = q.popleft()
        if cur == end:
            return dist[cur]
        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)
    return -1

print(bfs(a, b))