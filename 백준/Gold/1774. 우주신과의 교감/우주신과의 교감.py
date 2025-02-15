import sys
from math import sqrt
input = sys.stdin.readline

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
    
def union_parent(parent, x, y):
    rt1 = find_parent(parent, x)
    rt2 = find_parent(parent, y)
    if rt1 > rt2:
        parent[rt1] = rt2
    else:
        parent[rt2] = rt1
        
def get_dist(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

N, M = map(int, input().split())
nodes = [0]*(N+1)
for i in range(1, N+1):
    a, b = map(int, input().split())
    nodes[i] = (a, b)
edges = []
for i in range(1, N):
    for j in range(i+1,N+1):
        edges.append([get_dist(nodes[i], nodes[j]), i, j])
        
edges.sort()
parent = [i for i in range(N+1)]  

for _ in range(M):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
    
mst_val = 0
for c, a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        mst_val += c
print(f"{mst_val:.2f}")