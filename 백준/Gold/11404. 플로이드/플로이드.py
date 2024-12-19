import sys

n = int(input())
m = int(input())

INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 출발지와 도착지가 같은 경우 거리 비용은 0
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
            
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    # 시작 도시와 도착 도시를 연결하는 노선이 하나가 아닐 수 있음
    graph[a][b] = min(graph[a][b], c)
    
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
for a in range(1, n + 1):
    for b in range(1, n + 1):
        print(graph[a][b], end=" ") if graph[a][b] != INF else print(0, end=" ")
    print()
            