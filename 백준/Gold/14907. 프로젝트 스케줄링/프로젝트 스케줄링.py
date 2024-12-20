import sys
from collections import deque, defaultdict

data = sys.stdin.read().splitlines()

# 작업의 개수
N = len(data)
graph = defaultdict(list)
durations = {}
indegree = defaultdict(int)

# 조건 입력
for lines in data:
    arr = lines.split()
    # 작업 이름
    w = arr[0]
    durations[w] = int(arr[1])
    # 선행 작업이 있는 경우
    if len(arr) > 2:
        for pre in arr[2]:
            # 정보 입력
            graph[pre].append(w)
            indegree[w] += 1
            
q = deque()   
dp = {t: 0 for t in durations}
# 진입차수가 0이면 큐에 삽입
for i in durations:
    if indegree[i] == 0:
        q.append(i)
        dp[i] = durations[i]

while q:
    now = q.popleft()
    for n in graph[now]:
        dp[n] = max(dp[n], dp[now] + durations[n])
        indegree[n] -= 1
        if indegree[n] == 0:
            q.append(n)
            
print(max(dp.values()))