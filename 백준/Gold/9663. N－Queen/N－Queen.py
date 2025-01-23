def solve_n_queens(n):
    def backtrack(row):
        if row == n:
            nonlocal count
            count += 1
            return
        for c in range(n):
            if not cols[c] and not left_diag[row - c + n - 1] and not right_diag[row + c]:
                cols[c] = left_diag[row - c + n - 1] = right_diag[row + c] = True
                backtrack(row + 1)
                cols[c] = left_diag[row - c + n - 1] = right_diag[row + c] = False
        
    cols = [False] * n
    left_diag = [False] * (2*n - 1)
    right_diag = [False] * (2*n - 1)
    
    count = 0  # 배치 가능한 경우의 수
    backtrack(0)  # 0 행부터 배치
    return count


def main():
    n = int(input())
    print(solve_n_queens(n))
    

if __name__ == "__main__":
    main()