import sys
from math import sqrt
input = sys.stdin.readline

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x, y):
    root1 = find_parent(parent, x)
    root2 = find_parent(parent, y)
    if root1 > root2:
        parent[root1] = root2
    else:
        parent[root2] = root1
        

n = int(input())

positions = []
for i in range(n):
    x, y = map(float, input().split())
    positions.append((x, y))
    
edges = []
for i in range(n):
    for j in range(i + 1, n):
        a = positions[i]
        b = positions[j]
        dist = sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
        edges.append((dist, i, j))

mst_cost = 0
parent = [i for i in range(n)]
for cost, a, b in sorted(edges):
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        mst_cost += cost

print(mst_cost)