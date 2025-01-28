import sys
input = sys.stdin.readline

def matching(person):
    for notebook in graph[person]:
        if visited[notebook]: 
            continue
        visited[notebook] = True    
        if not matched[notebook] or matching(matched[notebook]):
            matched[notebook] = person
            return True
    return False

N, M = map(int, input().split())
matched = {notebook: 0 for notebook in range(1, N + 1)}
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    person, notebook = map(int, input().split())
    graph[person].append(notebook)

count = 0    
for person in range(1, N + 1):
    visited = [False] * (N + 1)
    if matching(person):
        count += 1
print(count)