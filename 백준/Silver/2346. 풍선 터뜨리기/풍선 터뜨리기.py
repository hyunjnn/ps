from collections import deque
from sys import stdin

n = int(input())
arr = enumerate(map(int, stdin.readline().split()))

queue = deque(arr)

res = []
for i in range(n):
    idx, move = queue.popleft()
    res.append(idx + 1)

    if move > 0:
        queue.rotate(-(move - 1))
    else:
        queue.rotate(-move)

print(*res)