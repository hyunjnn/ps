# 모든 간선의 비용을 더한 값에서 MST 비용을 뺀 값 만큼이 최대 절약 액수임
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
    while True:
        v, e = map(int, input().split())
        if v == 0 and e == 0:
            break
        
        edges = []
        total_cost = 0
        for _ in range(e):
            a, b, c = map(int ,input().split())
            total_cost += c
            edges.append((c, a, b))
            
        edges.sort()
        
        parent = [i for i in range(v)]
        mst_cost = 0
        for cost, a, b in edges:
            if find_parent(parent, a) != find_parent(parent, b):
                union_parent(parent, a, b)
                mst_cost += cost
        
        print(total_cost - mst_cost)
    

if __name__ == "__main__":
    main()