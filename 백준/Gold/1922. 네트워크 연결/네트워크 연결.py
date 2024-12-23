from heapq import heappush, heappop

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    

N = int(input())
M = int(input())
edges = []
parent = [i for i in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    heappush(edges, (c, a, b))

res = 0
while edges:
    cost, a, b = heappop(edges)
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += cost
print(res)
    