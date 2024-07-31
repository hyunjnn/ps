from sys import stdin

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, stdin.readline().split())))
arr.sort(key= lambda x: (x[0], x[1]))

for i in arr:
    print(*i)