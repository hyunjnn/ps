import sys
input = sys.stdin.readline
INF = int(1e9)

def solve(graph, n):
    # 이동 방향
    DIRECTIONS = [(1, 0), (0, 1)]
    # i, j 위치에 가기 위한 최소 비용
    dp = [[INF] * n for _ in range(n)]
    dp[0][0] = 0
    
    for x in range(n):
        for y in range(n):
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n:
                    # 현재 위치보다 작으면 추가 비용 없이 이동
                    if graph[x][y] > graph[nx][ny]:
                        dp[nx][ny] = min(dp[nx][ny], dp[x][y])
                    else:  # 차이만큼 버튼 누르는 비용 발생
                        dp[nx][ny] = min(dp[nx][ny], dp[x][y] + graph[nx][ny] - graph[x][y] + 1)
    # 최소 비용 반환
    return dp[n - 1][n - 1] 
    
    
def main():
    n = int(input())
    grid = [list(map(int, input().strip().split())) for _ in range(n)]
    print(solve(grid, n))
    

if __name__ == "__main__":
    main()
    