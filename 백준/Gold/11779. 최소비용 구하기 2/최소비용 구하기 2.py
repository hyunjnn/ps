from heapq import heappush, heappop

INF = int(1e9)
def dijkstra(graph, s, e):
    # 거리 정보
    distances = [INF] * len(graph)
    distances[s] = 0
    
    # 경로 추적 리스트
    parent = [-1] * len(graph)
    
    # 비용, 도시
    hq = [(0, s)]
    
    while hq:
        current_cost, current_node = heappop(hq)
        
        # 목적지에 도착한 경우 
        if current_node == e:
            break
            
        # 인접 노드 탐색
        for neighbor, w in graph[current_node]:
            new_cost = current_cost + w
            # 더 짧은 경로를 발견한 경우
            if new_cost < distances[neighbor]:
                heappush(hq, (new_cost, neighbor))
                # 거리 정보 업데이트
                distances[neighbor] = new_cost
                # 경로 업데이트
                parent[neighbor] = current_node
    # 경로 복원            
    path = []
    current = e
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()
    
    return path, current_cost    
    
# 도시의 개수
n = int(input())
# 버스의 개수
m = int(input())

# 그래프 정보 입력
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
# 출발, 도착 도시 입력
start, end = map(int, input().split())

# 최소비용 경로 탐색
path, cost = dijkstra(graph, start, end)

# 최소 비용
print(cost)

# 경로에 포함된 도시의 개수(출발 도시, 도착 도시 포함)
print(len(path))

# 경로 출력
print(" ".join(map(str, path)))