import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, graph, n):
    # i번 컴퓨터가 감염되기까지 걸리는 시간
    times = [INF] * (n + 1)
    # 시간, 감염된 컴퓨터
    q = [(0, start)]
    times[start] = 0
    while q:
        current_time, current_computer = heappop(q)
        if current_time > times[current_computer]:
            continue
        # 주변 컴퓨터로 감염 전파
        for neighbor, t in graph[current_computer]:
            nt = current_time + t
            if nt < times[neighbor]:
                times[neighbor] = nt
                heappush(q, (nt, neighbor))
    return times

    
def main():
    T = int(input())
    for _ in range(T):
        # 컴퓨터 개수, 의존성 개수, 해킹 컴퓨터 번호
        n, d, c = map(int, input().split())
        
        
        graph = [[] for _ in range(n + 1)]
        # 의존 정보 입력(단방향)
        for _ in range(d):
            # b 감염 -> s초 후 -> a 감염
            a, b, s = map(int, input().split())
            graph[b].append((a, s))
            
        times = dijkstra(c, graph, n)
        infected_count = sum(1 for t in times if t != INF)
        max_time = max(t for t in times if t != INF)
        
        # 감염된 컴퓨터 수, 마지막으로 감염되는 시간 출력
        print(infected_count, max_time)    
    
    
if __name__ == "__main__":
    main()
