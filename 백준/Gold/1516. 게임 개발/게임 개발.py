from collections import deque

# 건물의 종류 수
N = int(input())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)
durations = [0] * (N + 1)

# 조건 입력 
for i in range(1, N + 1):
    arr = list(map(int, input().split()))
    durations[i] = arr[0]
    for pre in arr[1:-1]:
        # 선행 정보 저장
        graph[pre].append(i)
        indegree[i] += 1

# 각 건물을 짓는데 걸리는 시간        
dp = [0] * (N + 1)
        
q = deque()
# 진입차수가 0이면 큐에 저장
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)
        dp[i] = durations[i]

# 위상 정렬
while q:
    now = q.popleft()
    for n in graph[now]:
        indegree[n] -= 1
        dp[n] = max(dp[n], dp[now] + durations[n])
        if indegree[n] == 0:
            q.append(n)
            
# 각 건물이 완성되기까지 걸리는 최소 시간 출력
print("\n".join(map(str, dp[1:])))            