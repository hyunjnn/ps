import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

sequence = []
res = 0

def backtrack(start, level):
    global res
    if sum(sequence) == S and level != 0:
        res += 1
        
    if start == N:
        return
    for i in range(start, N):
        sequence.append(nums[i])
        backtrack(i+1, level+1)
        sequence.pop()

        
backtrack(0, 0)        
print(res)