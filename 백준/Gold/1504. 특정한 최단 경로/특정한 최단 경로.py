from heapq import heappush, heappop
INF = int(1e9)

def bfs(start):
    dist = [INF] * (N + 1)
    # 현재 비용과 노드
    q = [(0, start)]
    dist[start] = 0
    
    while q:
        curr_dist, curr_node = heappop(q)
        for neighbor, distance in graph[curr_node]:
            new_dist = curr_dist + distance
            if dist[neighbor] > new_dist:
                dist[neighbor] = new_dist
                heappush(q, (new_dist, neighbor))
    
    return dist

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# 지나야 하는 두 정점    
x, y = map(int, input().split())

dist_from_1 = bfs(1)
dist_from_x = bfs(x)
dist_from_y = bfs(y)

# 1 -> x -> y -> N
p1 = dist_from_1[x] + dist_from_x[y] + dist_from_y[N]
# 1 -> y -> x -> N
p2 = dist_from_1[y] + dist_from_y[x] + dist_from_x[N]

res = min(p1, p2)
print(res if res < INF else -1)