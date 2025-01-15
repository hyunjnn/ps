import sys
input = sys.stdin.readline

def dfs(staff):
    # 해당 직원이 할 수 있는 모든 일 탐색
    for task in graph[staff]:
        if visited[task]: continue
        visited[task] = True
        # 아직 배정된 직원이 없거나 조정 가능한 경우
        if match[task] == 0 or dfs(match[task]):
            # 해당 직원을 배정
            match[task] = staff
            return True
    return False
    

# 직원, 할 일의 수
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    _, *task = input().split()
    graph[i].extend(map(int, task))

# 할 일 번호: 담당 직원 번호
match = {task: 0 for task in range(1, M + 1)}

res = 0
# 직원과 할 일 매칭
for staff in range(1, N + 1):
    visited = [False] * (M + 1)
    if dfs(staff):
        res += 1  # 매칭 성공
print(res)
    