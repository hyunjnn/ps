def solution(triangle):
    N = len(triangle)
    
    for row in range(1, N):
        for col in range(row+1):
            if col == 0:
                triangle[row][col] += triangle[row-1][col]
            elif col == row:
                triangle[row][col] += triangle[row-1][col-1]
            else:
                triangle[row][col] += max(triangle[row-1][col], triangle[row-1][col-1])
                
    return max(triangle[-1])