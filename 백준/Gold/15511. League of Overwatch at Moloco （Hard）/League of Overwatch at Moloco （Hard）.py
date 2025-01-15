from collections import deque
import sys
input = sys.stdin.readline

def is_bipartite(graph, n):
    tags = [0] * (n + 1)
    for start in range(1, n + 1):
        if tags[start] == 0: 
            q = deque([start])
            tags[start] = 1
            while q:
                curr = q.popleft()
                for adj in graph[curr]:
                    if tags[adj] == 0:
                        tags[adj] = -tags[curr]
                        q.append(adj)
                    elif tags[adj] == tags[curr]:
                        return False
    return True
    

V, E = map(int, input().split())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
print("POSSIBLE" if is_bipartite(graph, V) else "IMPOSSIBLE")