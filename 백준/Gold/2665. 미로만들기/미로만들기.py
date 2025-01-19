import sys
from collections import deque

input = sys.stdin.readline
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
INF = int(1e9)

def count_black(graph, n, start_x, start_y):
    costs = [[INF] * n for _ in range(n)]
    
    costs[start_x][start_y] = 0
    q = deque([(start_x, start_y)])
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < n:
                # black
                if graph[nx][ny] == 0 and costs[nx][ny] > costs[x][y] + 1:  
                    q.append((nx, ny))
                    costs[nx][ny] = costs[x][y] + 1
                # white
                elif graph[nx][ny] == 1 and costs[nx][ny] > costs[x][y]:
                    q.appendleft((nx, ny))
                    costs[nx][ny] = costs[x][y]
                    
    return costs[n - 1][n - 1]


def main():
    n = int(input())  # 방 개수
    graph = [list(map(int, input().strip())) for _ in range(n)]
    print(count_black(graph, n, 0, 0))
    
    
if __name__ == "__main__":
    main()