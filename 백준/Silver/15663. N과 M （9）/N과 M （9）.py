import sys
input = sys.stdin.readline

N, M = map(int, input().split())
sorted_nums = sorted(list(map(int, input().split())))

visited = [False] * N
sequence = []

def backtrack(level):
    if len(sequence) == M:
        print(*sequence)
        return
    
    pre = -1
    for i in range(N):
        if not visited[i] and pre != sorted_nums[i]: 
            visited[i] = True    
            sequence.append(sorted_nums[i])
            backtrack(level + 1)
            visited[i] = False
            sequence.pop()
            pre = sorted_nums[i]
    

backtrack(0)
