from heapq import heappush, heappop

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

# 규칙 입력
for _ in range(M):
    a, b = map(int, input().split())
    # a번 문제를 b번 문제보다 먼저 푸는 것이 좋음
    graph[a].append(b)
    indegree[b] += 1
 
# 위상정렬을 위한 큐(쉬운 문제를 먼저 풀어야 하므로 우선순위 큐를 사용함)
q = []
for i in range(1, N + 1):
    # 진입차수가 0이면 큐에 삽입
    if indegree[i] == 0:
        heappush(q, i)

res = []
while q:
    now = heappop(q)
    res.append(now)
    for n in graph[now]:
        indegree[n] -= 1
        # 진입차수가 0이면 큐에 삽입
        if indegree[n] == 0:
            heappush(q, n)

print(" ".join(map(str, res)))            