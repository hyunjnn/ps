from heapq import heappush, heappop

INF = int(1e9)

def dijkstra(start, end):
    # 위치 x에 도달하는데 걸린 시간 초기화
    dp = [INF] * 100001
    dp[start] = 0
    # 걸린 시간, 현재 위치
    hq = [(0, start)]
    
    while hq:
        current_time, current_x = heappop(hq)
        # 동생을 찾은 경우, 찾기까지 걸린 최소 시간 반환
        if current_x == end:
            return current_time
        
        for time, nx in [(1, current_x + 1), (1, current_x - 1), (0, current_x * 2)]:
            nt = current_time + time
            if 0 <= nx <= 100000 and nt < dp[nx]:
                heappush(hq, (nt, nx))
                dp[nx] = nt
                    
# 내 위치, 동생 위치                    
N, K = map(int, input().split())
# 동생을 찾는데 걸린 최소 시간 출력
print(dijkstra(N, K))