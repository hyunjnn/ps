import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def dijkstra(start):
    dist = [int(1e9)] * (D + 1)
    dist[0] = 0
    
    q = [(0, start)]
    while q:
        cost, now = heappop(q)
        if cost > dist[now]:
            continue
        for v, w in graph[now]:
            new_cost = cost + w
            if new_cost < dist[v]:
                dist[v] = new_cost
                heappush(q, (new_cost, v))
        
    return dist[D]


N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]
for i in range(D):
    graph[i].append((i+1, 1))
for _ in range(N):
    a, b, c = map(int, input().split())
    if b <= D:
        graph[a].append((b, c))
    
print(dijkstra(0))
    