from heapq import heappush, heappop

INF = int(1e9)
def dijkstra(graph, start):
    d = [INF] * len(graph)
    d[start] = 0
    hq = [(0, start)]
    while hq:
        current_weight, current_node = heappop(hq)
        if d[current_node] < current_weight:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_weight + weight
            if d[neighbor] > distance:
                d[neighbor] = distance
                heappush(hq, (distance, neighbor))
    return d

# 도시의 개수
N = int(input())
# 버스의 개수
M = int(input())

# 그래프 초기화
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

# 출발점, 도착점의 도시번호
start, end = map(int, input().split())

distances = dijkstra(graph, start)

# 출발 도시에서 도착 도시까지 가는데 드는 최소 비용 출력
print(distances[end])