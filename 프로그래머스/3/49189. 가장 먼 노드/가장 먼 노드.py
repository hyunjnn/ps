from collections import deque

def solution(n, edge):
    
    # 그래프 초기화
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    # 거리 정보 초기화
    distances = [-1] * (n + 1)
    
    # 1번 부터 시작
    dq = deque([1])
    distances[1] = 0
    
    while dq:
        current = dq.popleft()
        # 인접 노드 탐색
        for neighbor in graph[current]:
            # 아직 방문하지 않은 경우
            if distances[neighbor] == -1:
                # 거리 업데이트
                distances[neighbor] = distances[current] + 1
                dq.append(neighbor)
    
    return distances.count(max(distances))