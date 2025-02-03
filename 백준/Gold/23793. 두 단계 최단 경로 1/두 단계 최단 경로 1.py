import sys
from heapq import heappush, heappop
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    
x, y, z = map(int, input().split())

def dijkstra(start, target, passing=False):
    global y
    dist = [INF] * (N+1)
    dist[start] = 0
    q = [(0, start)]
    while q:
        cost, now = heappop(q)
        if cost > dist[now]:
            continue
        for v, w in graph[now]:
            if passing and v == y:
                continue
            new_cost = cost + w
            if new_cost < dist[v]:
                dist[v] = new_cost
                heappush(q, (new_cost, v))
    
    return dist[target] if dist[target] != INF else -1


d1 = dijkstra(x, y)
d2 = dijkstra(y, z)

d3 = dijkstra(x, z, passing=True)

print(d1+d2 if d1 != -1 and d2 != -1 else -1, d3)