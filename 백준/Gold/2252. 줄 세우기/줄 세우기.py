from collections import deque

n, m = map(int, input().split())
indgree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    # a가 b의 앞에 서야 함
    graph[a].append(b)
    indgree[b] += 1

q = deque()
for i in range(1, n + 1):
    # 처음에 진입차수가 0이면 큐에 넣음
    if indgree[i] == 0:
        q.append(i)
        
res = []        
while q:
    now = q.popleft()
    res.append(now)
    for neighbor in graph[now]:
        indgree[neighbor] -= 1
        if indgree[neighbor] == 0:
            q.append(neighbor)
    
print(" ".join(map(str, res)))