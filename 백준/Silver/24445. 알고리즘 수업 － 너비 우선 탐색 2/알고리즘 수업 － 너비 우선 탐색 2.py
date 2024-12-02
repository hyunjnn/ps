from collections import deque

def bfs(graph, start, visited):
    # 방문 순서 카운트
    count = 1
    # 방문 노드 저장 리스트
    res = [0] * len(graph)
    res[start] = count
    # 시작 노드 방문 처리
    dq = deque([start])
    visited[start] = True
    
    # 인접 노드 방문
    while dq:
        q = dq.popleft()
        for neighbor in graph[q]:
            if not visited[neighbor]:
                count += 1
                dq.append(neighbor)
                visited[neighbor] = True
                res[neighbor] = count
              
    return res

# 정점의 수 , 간선의 수, 시작 정점
N, M, R = map(int, input().split())

# 그래프 정보 입력
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 그래프 정렬(내림차순)
for g in graph:
    g.sort(reverse=True)
    
visited = [False] * (N + 1)

# 노드 방문 순서 계산
res = bfs(graph, R, visited)

# 각 노드 방문 순서 출력
print("\n".join(list(map(str, res[1:]))))  