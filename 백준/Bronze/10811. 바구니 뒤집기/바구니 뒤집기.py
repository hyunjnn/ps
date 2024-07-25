N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, input().split())
    tmp = arr[i-1:j:1]
    tmp.reverse()
    arr[i-1:j:1] = tmp

print(*arr)