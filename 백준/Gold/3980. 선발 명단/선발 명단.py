import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    
    max_val = -sys.maxsize
    board = [list(map(int, input().split())) for _ in range(11)]
    used = [False]*11
    
    def backtrack(total, row):
        global max_val
        
        if row == 11:
            max_val = max(max_val, total)
            return
        
        for col in range(11):
            if board[row][col] != 0 and not used[col]:
                used[col] = True
                backtrack(total+board[row][col], row+1)
                used[col] = False
                
    backtrack(0, 0)        
    print(max_val)       