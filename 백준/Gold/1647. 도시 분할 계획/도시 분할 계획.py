import sys
from heapq import heappush, heappop

N, M = map(int, input().split())
edges = []
for _ in range(M):
    A, B, C = map(int, sys.stdin.readline().strip().split())
    heappush(edges, (C, A, B))

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]
    
def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

parent = [i for i in range(N + 1)]
res_edges = []
# 최소 유지비의 합
res = 0
while edges:
    cost, a, b = heappop(edges)
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        res += cost
        heappush(res_edges, -cost)
print(res - (-heappop(res_edges)))