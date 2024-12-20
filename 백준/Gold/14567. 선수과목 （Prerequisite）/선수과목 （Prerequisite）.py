from collections import deque

# 과목의 수, 선수 조건의 수
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

# 조건 입력
for _ in range(M):
    a, b = map(int, input().split())
    # a 과목은 b 과목의 선수과목
    graph[a].append(b)
    # b의 진입차수 증가
    indegree[b] += 1

# 각 과목을 이수할 수 있는 최소 학기 
dp = [0] * (N + 1)    
    
# 위상 정렬을 위한 큐
q = deque()
for i in range(1, N + 1):
    # 진입차수가 0이면 큐에 삽입
    if indegree[i] == 0:
        q.append(i)
        dp[i] = 1

while q:
    now = q.popleft()
    for n in graph[now]:
        indegree[n] -= 1
        dp[n] = dp[now] + 1
        if indegree[n] == 0:
            q.append(n)

# 각 과목별 이수 가능한 최소 학기 출력
print(" ".join(map(str, dp[1:])))           