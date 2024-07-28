import sys

paper = [[0 for _ in range(100)] for _ in range(100)]
N = int(input())

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    for j in range(a, a + 10):
        for k in range(b, b + 10):
            paper[j][k] = 1
count = 0
for row in paper:
    count += row.count(1)
print(count)