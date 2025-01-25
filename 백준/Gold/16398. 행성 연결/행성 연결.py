import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x, y):
    a = find_parent(parent, x)
    b = find_parent(parent, y)
    if a < b:
        parent[b] = a
    elif a > b:
        parent[a] = b

        
n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

edges = []
for i in range(n):
    for j in range(n):
        if i != j:
            edges.append((costs[i][j], i, j))
    
mst_cost = 0
parent = [i for i in range(n)]
for cost, x, y in sorted(edges):
    if find_parent(parent, x) != find_parent(parent, y):
        mst_cost += cost
        union_parent(parent, x, y)
        
print(mst_cost)