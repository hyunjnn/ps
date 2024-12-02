n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    prev2 = 1
    prev1 = 2
    for _ in range(3, n + 1):
        current = (prev2 + prev1) % 10007
        prev2 = prev1
        prev1 = current
    print(current)    
