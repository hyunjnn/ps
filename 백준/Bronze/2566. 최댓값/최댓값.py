import sys

grid = [list(map(int, sys.stdin.readline().strip().split()))
        for _ in range(9)]
max_val = 0
row = 0
col = 0
for i in range(9):
    for j in range(9):
        if grid[i][j] > max_val:
            max_val = grid[i][j]
            row = i
            col = j
print(max_val)
print(row + 1, col + 1)