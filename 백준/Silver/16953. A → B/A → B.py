from collections import deque

def bfs(a, b):
    # 현재 수, 연산 횟수 저장
    dq = deque([(a, 0)])
    visited = set([a])
    
    while dq:
        current_num, count = dq.popleft()
        
        # 목표 숫자에 도달한 경우 
        if current_num == b:
            return count + 1
        
        for x in [current_num * 2, current_num * 10 + 1]:
            if 1 <= x <= 1000000000 and x not in visited:
                    dq.append((x, count + 1))
                    visited.add(x)
    return -1

A, B = map(int, input().split())
print(bfs(A, B))