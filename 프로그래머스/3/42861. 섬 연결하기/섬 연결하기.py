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

def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    
    costs.sort(key=lambda x: x[2])
        
    for i, j, c in costs:
        if find_parent(parent, i) != find_parent(parent, j):
            union_parent(parent, i, j)
            answer += c
    
    return answer