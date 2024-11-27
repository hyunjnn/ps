from collections import deque

def bfs(height, start, end, up, down):
    # 시작 층, 이동 횟수 저장
    dq = deque([(start, 0)])
    visited = {start}
    
    while dq:
        current, count = dq.popleft()
        
        # 원하는 층에 도착한 경우, 이동 횟수 반환
        if current == end:
            return count
        
        for x in [current + up, current - down]:
            if 1 <= x <= height and not x in visited:
                dq.append((x, count + 1))
                visited.add(x)
        
    return "use the stairs"  # 엘리베이터로 이동 불가한 경우


# 총 층수, 현재 층, 가고 싶은 층, 위로 이동하는 층, 아래로 이동하는 층
F, S, G, U, D = map(int, input().split())
# 이동 횟수 출력
print(bfs(F, S, G, U, D))
