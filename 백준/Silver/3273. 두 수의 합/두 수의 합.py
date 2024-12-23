import sys
from itertools import combinations

n = int(input())
arr = list(map(int, sys.stdin.readline().strip().split()))
x = int(input())

arr.sort()

start, end, count = 0, n - 1, 0

while start < end:
    current = arr[start] + arr[end]
    if current == x:
        count += 1
        start += 1
        end -= 1
    elif current < x:
        start += 1
    else:
        end -= 1
        
print(count)