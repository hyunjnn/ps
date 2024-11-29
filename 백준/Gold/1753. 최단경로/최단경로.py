from heapq import heappush, heappop

INF = int(1e9)
def dijkstra(graph, start):
    # 거리값 무한으로 초기화
    d = [INF] * len(graph)
    d[start] = 0
    # 가중치, 시작점 
    hq = [(0, start)]
    while hq:
        current_weight, current_node = heappop(hq)
        # 이미 방문한 경우 무시
        if d[current_node] < current_weight:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_weight + weight
            if distance < d[neighbor]:
                d[neighbor] = distance
                heappush(hq, (distance, neighbor))
    
    return d


# 정점, 간선 개수
V, E = map(int, input().split())
# 시작 정점 번호
K = int(input())

# 그래프 정보 입력
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distance = dijkstra(graph, K)

for i in range(1, V + 1):
    # 최단 경로의 경로값 출력
    print(distance[i]) if distance[i] != INF else print("INF")