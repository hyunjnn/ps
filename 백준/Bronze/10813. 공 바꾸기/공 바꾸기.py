import sys

N, M = map(int, input().split())
arr = [i + 1 for i in range(N)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    arr[i - 1], arr[j - 1] = arr[j - 1], arr[i - 1]

print(*arr)