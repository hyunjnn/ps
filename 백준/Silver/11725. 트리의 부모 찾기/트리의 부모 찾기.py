from collections import deque

N = int(input())

graph = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])
parent[1] = 1

while q:
    node = q.popleft()
    for child in graph[node]:
        if parent[child] == 0:
            parent[child] = node
            q.append(child)
            
print("\n".join(map(str, parent[2:])))