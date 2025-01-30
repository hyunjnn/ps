import sys
input = sys.stdin.readline

while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
        
    sequence = []
    
    def backtrack(cur, level):
        if level == 6:
            print(" ".join(map(str, sequence)))
            return
        
        for i in range(cur, len(nums)):
            sequence.append(nums[i])
            backtrack(i+1, level+1)
            sequence.pop()
       
    backtrack(1, 0)
    print()