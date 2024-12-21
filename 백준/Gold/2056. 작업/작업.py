from collections import deque
import sys

# 수행해야 할 작업의 개수
N = int(input())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

# 해당 작업 시간
durations = [0] * (N + 1)

# 선행 조건 입력
for i in range(1, N + 1):
    data = list(map(int, sys.stdin.readline().strip().split()))
   
    # 해당 작업에 걸리는 시간 
    durations[i] = data[0]
    
    # 선행 작업이 없는 경우
    if data[1] == 0:
        continue
    # 선행 관계에 있는 작업 번호
    for pre in data[2:]:
        graph[pre].append(i)
        indegree[i] += 1
        
dp = [0] * (N + 1)
q = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)
        dp[i] = durations[i]

while q:
    now = q.popleft()
    for n in graph[now]:
        indegree[n] -= 1
        dp[n] = max(dp[n], dp[now] + durations[n])
        if indegree[n] == 0:
            q.append(n)
print(max(dp))           