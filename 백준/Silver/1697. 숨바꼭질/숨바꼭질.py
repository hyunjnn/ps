from collections import deque

def bfs(start, end, visited):
    # 시작 지점, 이동 횟수 저장
    dq = deque([(start, 0)])
    visited[start] = True
    while dq:
        current, count = dq.popleft()
        if current == end:
            return count
        for x in [current + 1, current - 1, current * 2]:
            if 0 <= x < 100001 and not visited[x]:
                dq.append((x, count + 1))
                visited[x] = True
    
    
N, K = map(int, input().split())
visited = [False] * 100001
print(bfs(N, K, visited))