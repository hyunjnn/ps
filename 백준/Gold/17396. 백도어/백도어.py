import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = sys.maxsize

def find_shortest_time(graph, n, is_visible):
    # 각 위치까지 걸리는 최소 시간
    times = [INF] * n
    times[0] = 0
    
    # 현재 시간, 위치
    hq = [(0, 0)]
    
    while hq:
        cur_time, cur_node = heappop(hq)
        if cur_time > times[cur_node]:
            continue
        for neighbor, cost in graph[cur_node]:
            if neighbor != n - 1 and is_visible[neighbor] == 1: 
                continue
            new_time = cur_time + cost
            if new_time < times[neighbor]:
                times[neighbor] = new_time
                heappush(hq, (new_time, neighbor))
    
    # 최소 시간 반환, 갈 수 없으면 -1
    return times[n - 1] if times[n - 1] != INF else -1


def main():
    v, e = map(int, input().split())
    is_visible = list(map(int, input().split()))
    
    graph = [[] for _ in range(v)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
        
    print(find_shortest_time(graph, v, is_visible))

    
if __name__ == "__main__":
    main()
    