import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n = int(input())

graph = defaultdict(list)
in_degree = defaultdict(int)
dwarves = set()

for _ in range(n):
    a, op, b = input().split()
    dwarves.update([a, b])
    if op == "<":
        graph[b].append(a)
        in_degree[a] += 1
    elif op == ">":
        graph[a].append(b)
        in_degree[b] += 1

for dwarf in dwarves:
    if dwarf not in in_degree:
        in_degree[dwarf] = 0
        
q = deque()      
for dwarf in dwarves:
    if in_degree[dwarf] == 0:
        q.append(dwarf)
        
count = 0
while q:
    now = q.popleft()
    count += 1
    for neighbor in graph[now]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            q.append(neighbor)

print("impossible" if count < len(dwarves) else "possible")