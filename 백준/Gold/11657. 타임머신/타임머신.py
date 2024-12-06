# 도시의 개수, 버스 노선의 개수
N, M = map(int, input().split())

# 버스 노선 정보 입력
edges = []
for _ in range(M):
    # a 도시에서 b 도시로 가는 비용 c
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

INF = int(1e9)
# 최단 경로 테이블 초기화
distances = [INF] * (N + 1)

def bellman_ford(start):
    distances[start] = 0
    for i in range(N):
        for current_node, next_node, cost in edges:
            if distances[current_node] != INF and distances[next_node] > distances[current_node] + cost:
                distances[next_node] = distances[current_node] + cost
                if i == N - 1:
                    return True
    return False
    
    
# 최단 경로 시간 탐색
res = bellman_ford(1)
if res:
    print(-1)
else:
    # 1에서 출발해 각 도시까지 가는 최단 시간 출력(경로가 없는 경우 -1 출력)
    for i in distances[2:]:
        print(i) if i != INF else print(-1)