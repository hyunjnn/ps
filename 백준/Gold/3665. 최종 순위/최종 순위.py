import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    
    n = int(input())
    ranking = list(map(int, input().split()))
    
    # [순위가 높은 팀] -> [낮은 팀, ... ]
    graph = [[] for _ in range(n + 1)]
    indegree = [0 for _ in range(n + 1)]
    
    for i, team in enumerate(ranking):
        for lower_team in ranking[i + 1:]:
            graph[team].append(lower_team)
            indegree[lower_team] += 1
    
    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        if a in graph[b]:
            graph[b].remove(a)
            indegree[a] -= 1
            graph[a].append(b)
            indegree[b] += 1
        elif b in graph[a]:
            graph[a].remove(b)
            indegree[b] -= 1
            graph[b].append(a)
            indegree[a] += 1
        
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
    
    res = []  
    is_certain = True
    
    while q:
        if len(q) > 1: # 진입 차수가 하나 이상이면 모호한 순위가 있음
            is_certain = False
        team = q.popleft()
        res.append(team)  # 순위가 높은 팀부터 저장
        for lower_team in graph[team]:
            indegree[lower_team] -= 1
            if indegree[lower_team] == 0:
                q.append(lower_team)
                
                
    if len(res) < n:  # 모든 노드를 순회하지 못함(사이클 발생)
        print("IMPOSSIBLE")
    elif not is_certain:
        print("?")
    else:
        print(" ".join(map(str, res)))