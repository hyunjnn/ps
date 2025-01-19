import sys
input = sys.stdin.readline
INF = int(1e9)
    
def main():
    n, m, r = map(int, input().split())
    items = list(map(int, input().split()))
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        graph[i][i] = 0

    for _ in range(r):
        a, b, c = map(int, input().split())
        graph[a][b] = min(graph[a][b], c)
        graph[b][a] = min(graph[b][a], c)
        
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
                
    max_items = 0
    for i in range(1, n + 1):
        total_items = 0
        for j in range(1, n + 1):
            if graph[i][j] <= m:
                total_items += items[j - 1]
        max_items = max(max_items, total_items)
     
    print(max_items)

if __name__ == "__main__":
    main()