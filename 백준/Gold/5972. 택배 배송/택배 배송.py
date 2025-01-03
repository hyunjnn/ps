from heapq import heappush, heappop

INF = int(1e9)
def bfs(start, end):
    # 시작 비용과 헛간
    q = [(0, start)]
    distances[start] = 0
    
    while q:
        current_dist, current_node = heappop(q)
        
        for neighbor, cost in graph[current_node]:
            new_distance = current_dist + cost
            # 더 적은 비용으로 갈 수 있는 경우
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heappush(q, (new_distance, neighbor))
        

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
distances = [INF] * (N + 1)

# 최소 비용 계산
bfs(1, N)

print(distances[N])