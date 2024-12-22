import sys
from heapq import heappop, heappush
sys.setrecursionlimit(10**5)

V, E = map(int, input().split())
edges = []

for _ in range(E):
    A, B, C = map(int, input().split())
    heappush(edges,(C, A, B))
    
parent = [x for x in range(V + 1)]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
    
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

res = 0
while edges:
    cost, a, b = heappop(edges)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += cost
        
print(res)