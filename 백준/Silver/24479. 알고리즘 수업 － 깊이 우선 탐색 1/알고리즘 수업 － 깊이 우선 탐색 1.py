import sys

def dfs(graph, start, visited, order):
    # 방문 순서 카운트
    count = 1
    stack = [start]
    
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = True
            order[v] = count
            count += 1
            # 인접 노드 탐색
            for neighbor in graph[v]:
                if not visited[neighbor]:
                    stack.append(neighbor)

        
# 정점의 수, 간선의 수, 시작 정점
N, M, R = map(int, input().split())

# 그래프 정보 입력
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, sys.stdin.readline().strip().split())
    graph[u].append(v)
    graph[v].append(u)
    
# 인접 정점을 오름차순으로 방문하기 위한 내림차순 정렬(dfs 스택 사용 때문)
for g in graph:
    g.sort(reverse=True)
    
# 방문 여부, 순서 저장 리스트 초기화
visited = [False] * (N + 1)
order = [0] * (N + 1)

# 그래프 탐색
dfs(graph, R, visited, order)

# 각 노드 별 방문 순서 출력
print("\n".join(map(str, order[1:])))