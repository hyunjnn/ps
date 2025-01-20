import sys
from heapq import heappush, heappop

input = sys.stdin.readline
DIRECTIONS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
INF = int(1e9)

def dijkstra(maps, n):
    dp = [[INF] * n for _ in range(n)]
    
    q = [(maps[0][0], 0 , 0)]
    dp[0][0] = maps[0][0]
    
    while q:
        cost, x, y = heappop(q)
        if cost > dp[x][y]:
            continue
            
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + maps[nx][ny] 
                if new_cost < dp[nx][ny]:
                    dp[nx][ny] = new_cost
                    heappush(q, (new_cost, nx, ny))
            
    return dp[n - 1][n - 1]
    
    
def main():
    problem_num = 1
    while True:
        n = int(input())
        
        if n == 0:
            break
            
        grid = [list(map(int, input().split())) for _ in range(n)]
        
        res = dijkstra(grid, n)
        print(f"Problem {problem_num}: {res}")
        problem_num += 1

        
if __name__ == "__main__":
    main()