import sys

N, M = map(int, input().split())
arr1 = [sys.stdin.readline().strip() for _ in range(N)]
arr2 = [sys.stdin.readline().strip() for _ in range(M)]
res = set(arr1) & set(arr2)
print(len(res))
for name in sorted(res):
    print(name)