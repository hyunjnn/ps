def dfs(graph, start, visited, order):
    # 방문 순서 카운트
    count = 1
    # 시작 노드 삽입
    st = [start]
    
    while st:
        v = st.pop()
        if not visited[v]:
            # 방문 처리
            visited[v] = True
            order[v] = count
            count += 1
            # 인접 노드 탐색
            for n in graph[v]:
                if not visited[n]:
                    st.append(n)

    
# 정점의 수, 간선의 수, 시작 정점
N, M, R = map(int, input().split())

# 그래프 정보 입력
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 인접 정점을 내림차순으로 방문하기 위한 오름차순 정렬(dfs 스택 사용때뭉)
for g in graph:
    g.sort()

# 방문 여부 리스트, 방문 순서 저장 리스트 초기화
visited = [False] * (N + 1)
order = [0] * (N + 1)

# 그래프 탐색
dfs(graph, R, visited, order)

# 각 노드별 방문 순서 출력
print("\n".join(map(str, order[1:])))