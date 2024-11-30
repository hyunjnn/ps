from collections import deque

def bfs(graph, start, visited):
    hq = deque([start])
    visited[start] = True
    res = [start] 
    cnt = 0
    while hq:
        q = hq.popleft()
        for n in sorted(graph[q]):
            if not visited[n]:
                cnt += 1
                hq.append(n)
                visited[n] = True
                res.append(n)
    return res

# 정점의 수, 간선의 수, 시작 정점
N, M, R = map(int, input().split())

# 그래프 정보 입력
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u ,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
# 방문 리스트 초기화    
visited = [False] * (N + 1)
# 그래프 탐색
nodes =  bfs(graph, R, visited)
s = 1
res = {x: 0 for x in range(1, N + 1)}
for node in nodes:
    res[node] = s
    s += 1
for x in res.items():
    print(x[1])