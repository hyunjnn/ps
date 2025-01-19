import sys
from collections import deque

input = sys.stdin.readline
DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
INF = int(1e9)


def count_black(graph, n, start_x, start_y):
    costs = [[INF] * n for _ in range(n)]
    
    costs[start_x][start_y] = True
    dq = deque([(0, start_x, start_y)])
    
    while dq:
        cost, x, y = dq.popleft()
        if cost > costs[x][y]:
            continue
        
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + (1 if graph[nx][ny] == 0 else 0)
                
                if new_cost < costs[nx][ny]:
                    costs[nx][ny] = new_cost
                    
                    if graph[nx][ny] == 0:  # black
                        dq.append((new_cost, nx, ny))
                    else:
                        dq.appendleft((new_cost, nx, ny))
                    
    return costs[n - 1][n - 1]


def main():
    n = int(input())  # 방 개수
    graph = [list(map(int, input().strip())) for _ in range(n)]
    print(count_black(graph, n, 0, 0))
    
    
if __name__ == "__main__":
    main()