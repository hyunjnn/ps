max_val = -int(1e9)
min_val = int(1e9)

N = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))

operations = {
    0: lambda x,y: x+y,
    1: lambda x,y: x-y,
    2: lambda x,y: x*y,
    3: lambda x,y: -(-x//y) if x<0 else x//y,
}

def backtrack(index, cur):
    global max_val, min_val
    if index == N:
        max_val = max(max_val, cur)
        min_val = min(min_val, cur)
        return
    
    for i in range(4):
        if op[i] > 0:
            op[i] -= 1
            backtrack(index+1, operations[i](cur, nums[index]))
            op[i] += 1
    
    
backtrack(1, nums[0])    
print(max_val)
print(min_val)
