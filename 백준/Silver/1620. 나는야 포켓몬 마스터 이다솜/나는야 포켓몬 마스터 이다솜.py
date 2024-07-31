from sys import stdin

input = stdin.readline

n ,m = map(int, input().split())
dict = {}
for i in range(1, n + 1):
    name = input().strip()
    dict[name] = str(i)
    dict[str(i)] = name

for j in range(m):
    k = input().strip()
    print(dict[k])