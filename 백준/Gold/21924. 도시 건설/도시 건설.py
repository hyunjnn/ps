import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:    
        parent[x] = y


def main():        
    N, M = map(int, input().split())

    edges = []
    total_cost = 0
    for _ in range(M):
        a, b, c = map(int, input().split())
        edges.append((c, a, b))
        total_cost += c
    
    parent = [i for i in range(N + 1)]
    min_cost = edge_cnt = 0

    for c, a, b in sorted(edges):
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            min_cost += c
            edge_cnt += 1
            
    print(total_cost - min_cost if edge_cnt == N - 1 else -1)

    
if __name__ == "__main__":
    main()