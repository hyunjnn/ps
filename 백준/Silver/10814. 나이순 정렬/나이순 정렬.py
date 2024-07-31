from sys import stdin

n = int(input())
arr = []
for i in range(n):
    age, name = stdin.readline().split()
    arr.append([age, name])

arr.sort(key= lambda x: int(x[0]))

for i in arr:
    print(*i)