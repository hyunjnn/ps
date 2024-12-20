from collections import deque

# 테스트케이스 개수
T = int(input())
for _ in range(T):
    
    # 건물의 개수, 건설 규칙의 수
    N, K = map(int, input().split())
    
    # 각 건물당 건설에 걸리는 시간
    durations = [0] + list(map(int, input().split()))
    
    indegree = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    
    # 건물순서 규칙 입력
    for _ in range(K):
        x, y = map(int, input().split())
        # 건물 x를 지은 다음 건물 y를 짓는 것이 가능함
        graph[x].append(y)
        indegree[y] += 1
    
    # 건설해야 할 건물의 번호 입력
    w = int(input())
    
    # 각 건물을 짓는데 걸리는 최소 시간 저장
    dp = [0] * (N + 1)
    
    # 위상 정렬을 위한 큐
    q = deque()
    for i in range(1, N + 1):
        # 진입차수가 0이면 큐에 삽입
        if indegree[i] == 0:
            q.append(i)
            dp[i] = durations[i]
            
    while q:
        now = q.popleft()
        for neighbor in graph[now]:
            indegree[neighbor] -= 1
            dp[neighbor] = max(dp[neighbor], dp[now] + durations[neighbor])
            if indegree[neighbor] == 0:
                q.append(neighbor)
                
    # 건물 w를 건설하는데 드는 최소 시간 출력
    print(dp[w])