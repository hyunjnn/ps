import sys

# 표의 크기, 합을 구해야 하는 횟수
N, M = map(int, input().split())

grid = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
prefix_sum = [[0] * N for _ in range(N)]

# 누적합 계산
for i in range(N):
    for j in range(N):
        prefix_sum[i][j] = grid[i][j]
        if i > 0:
            prefix_sum[i][j] += prefix_sum[i-1][j]
        if j > 0:
            prefix_sum[i][j] += prefix_sum[i][j-1]
        if i > 0 and j > 0:
            prefix_sum[i][j] -= prefix_sum[i-1][j-1]

def f(x1, y1, x2, y2):
    res = prefix_sum[x2][y2]
    if x1 > 0:
        res -= prefix_sum[x1-1][y2]
    if y1 > 0:
        res -= prefix_sum[x2][y1-1]
    if x1 > 0 and y1 > 0:
        res += prefix_sum[x1-1][y1-1]
    return res

    
# 구간합 계산
for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
    print(f(x1-1, y1-1, x2-1, y2-1))
    