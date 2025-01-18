from heapq import heappush, heappop
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, graph, n):
    dp = [INF] * (n + 1)
    q = [(0, start)]
    dp[start] = 0
    while q:
        cur_cost, cur_node = heappop(q)
        if cur_cost > dp[cur_node]:
            continue
        for neighbor, cost in graph[cur_node]:
            new_cost = cur_cost + cost
            if new_cost < dp[neighbor]:
                dp[neighbor] = new_cost
                heappush(q, (new_cost, neighbor))
    return dp
    
    
def main():
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
        
    s, t = map(int, input().split())
    costs = dijkstra(s, graph, v)
    print(costs[t])

if __name__ == "__main__":
    main()
