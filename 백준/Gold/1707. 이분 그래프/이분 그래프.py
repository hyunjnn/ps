from collections import deque
import sys
input = sys.stdin.readline

def isBipartite(graph, n):
    colors = [0] * (n + 1)  # 0 if not visited else 1 or -1
    
    # 비연결 그래프 고려 모든 노드 탐색
    for start in range(1, n + 1):
        if colors[start] != 0: 
            continue  # 이미 방문한 경우 무시
            
        # 방문 처리
        q = deque([start])
        colors[start] = 1
        
        while q:
            current_node = q.popleft()
            for neighbor in graph[current_node]:
                # 방문하지 않은 인접 노드는 다른 색으로 칠함
                if colors[neighbor] == 0:
                    q.append(neighbor)
                    colors[neighbor] = -colors[current_node]
                # 인접 노드와 색이 같다면 이분 그래프가 아님
                elif colors[neighbor] == colors[current_node]:
                    return False
    return True
    
    
# 테스트 횟수
K = int(input())
for _ in range(K):
    
    # 정점, 간선의 개수
    v, e = map(int, input().split())
    
    # 그래프 초기화
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    # 이분 그래프 판별 
    print("YES" if isBipartite(graph, v) else "NO")
    