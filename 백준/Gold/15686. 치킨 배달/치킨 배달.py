import sys
from itertools import combinations
input = sys.stdin.readline
INF = int(1e9)

def get_positions(grid, n):
    house_positions = []
    chicken_positions = []
    for x in range(n):
        for y in range(n):
            if grid[x][y] == 1:
                house_positions.append((x, y))
            elif grid[x][y] == 2:
                chicken_positions.append((x, y))
    return house_positions, chicken_positions


def calc_city_dist(house_positions, chicken_positions):
    total_dist = 0
    for hx, hy in house_positions:
        min_dist = INF
        for cx, cy in chicken_positions:
            min_dist = min(min_dist, abs(hx-cx) + abs(hy-cy))
        total_dist += min_dist
    return total_dist
    

def main():
    N, M = map(int, input().split())
    city_map = [list(map(int, input().split())) for _ in range(N)]
    
    house_positions, chicken_positions = get_positions(city_map, N)

    min_city_dist = INF
    for selected in combinations(chicken_positions, M):
        dist = calc_city_dist(house_positions, selected)
        min_city_dist = min(min_city_dist, dist)
    print(min_city_dist)
    

if __name__ == "__main__":
    main()