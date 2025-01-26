import sys
from itertools import combinations
input = sys.stdin.readline
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def solve():
    N = int(input())
    grid = [list(input().split()) for _ in range(N)]

    #student_positions = []
    teacher_positions = []
    empty_spaces = []

    # 빈 공간, 선생님 위치 찾기
    for x in range(N):
        for y in range(N):
            if grid[x][y] == "X":
                empty_spaces.append((x, y))
            elif grid[x][y] == "T":
                teacher_positions.append((x, y))

    def simulation(grid, teacher_positions):
        def watch(x, y, direction):
            nx, ny = x, y
            while True:
                nx += direction[0]
                ny += direction[1]
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    break
                if grid[nx][ny] == "O":
                    break
                if grid[nx][ny] == "S":
                    return True
            return False
            
        for tx, ty in teacher_positions:
            for d in DIRECTIONS:
                if watch(tx, ty, d):
                    return False
        return True
                
    # 빈 공간 중 장애물을 배치할 위치를 찾아 시뮬레이션 진행
    for obstacle_positions in combinations(empty_spaces, 3):
        for x, y in obstacle_positions:
            grid[x][y] = "O"
        if simulation(grid, teacher_positions):
            print("YES")
            return
        for x, y in obstacle_positions:
            grid[x][y] = "X"

    print("NO")        
    
solve()