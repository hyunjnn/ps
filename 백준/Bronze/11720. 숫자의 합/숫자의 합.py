import sys

N = int(input())
num = list(map(int, sys.stdin.readline().strip()))
sum = 0
for i in num:
    sum += i
    
print(sum)