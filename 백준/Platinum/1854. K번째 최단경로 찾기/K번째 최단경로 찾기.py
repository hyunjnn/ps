import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def k_shortest_path(start):
    distances = [[] for _ in range(n + 1)]
    heap = []
    
    heappush(heap, (0, start))
    heappush(distances[start], 0)
    
    while heap:
        current_cost, current_node = heappop(heap)
        
        for neighbor, cost in graph[current_node]:
            new_cost = current_cost + cost
            if len(distances[neighbor]) < k:
                heappush(heap, (new_cost, neighbor))
                heappush(distances[neighbor], -new_cost)
            # 더 짧은 거리가 있는 경우    
            elif new_cost < -distances[neighbor][0]:
                heappop(distances[neighbor])
                heappush(heap, (new_cost, neighbor))
                heappush(distances[neighbor], -new_cost)
                    
    return distances
    
dist = k_shortest_path(1)

for i in range(1, n + 1):
    print(-dist[i][0] if len(dist[i]) >= k else -1)