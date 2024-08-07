from collections import deque

# 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 각 도시 까지의 최단 거리를 저장할 리스트
distance = [-1] * (n + 1)
# 출발 도시
distance[x] = 0

q = deque([x])
while q:
    v = q.popleft()
    for next_city in graph[v]:
        if distance[next_city] == -1:
            distance[next_city] = distance[v] + 1
            q.append(next_city)

check = False
for i in range(1, n + 1):
    # 도달 가능한 도시 중 최단 거리가 k인 모든 도시 번호 출력
    if distance[i] == k:
        print(i)
        check = True

if not check:
    # 조건에 해당하는 도시가 하나도 존재하지 않는 경우
    print(-1)
