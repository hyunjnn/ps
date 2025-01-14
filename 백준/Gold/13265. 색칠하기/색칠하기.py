import sys
from collections import deque
input = sys.stdin.readline

def isBipartite(graph, v):
    colors = [0] * (v + 1)
    
    for start_node in range(1, v + 1):
        if colors[start_node] != 0: 
            continue
            
        q = deque([start_node])
        colors[start_node] = 1
        while q:
            current_node = q.popleft()
            
            for neighbor in graph[current_node]:
                if colors[neighbor] == 0:
                    colors[neighbor] = -colors[current_node]
                    q.append(neighbor)
                    
                elif colors[current_node] == colors[neighbor]:
                    return False
    return True
    

T = int(input())
for _ in range(T):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
        
    print("possible" if isBipartite(graph, v) else "impossible")
        