import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

dist = [[INF]*(n+1) for _ in range(n+1)]
# 최단 경로에서 처음 방문하는 노드 저장
routing_table = [['-'] * (n+1) for _ in range(n+1)] 

for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = dist[b][a] = c
    routing_table[a][b], routing_table[b][a] = b, a
    
for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if i != j and dist[i][j] > dist[i][k]+dist[k][j]:
                # 최단 거리 갱신 시, 첫 방문 노드도 업데이트
                dist[i][j] = dist[i][k]+dist[k][j]
                routing_table[i][j] = routing_table[i][k]
            
for row in routing_table[1:]:
    print(" ".join(map(str, row[1:])))