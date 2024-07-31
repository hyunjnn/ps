from sys import stdin

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(stdin.readline()))
arr.sort()
for i in arr:
    print(i)