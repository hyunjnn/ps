import sys
input = sys.stdin.readline

N = int(input())
egg = []
for _ in range(N):
    durability, weight = map(int, input().split())
    egg.append([durability, weight])
    
def backtrack(start):
    if start == N:
        global max_val
        # 깨진 계란의 수
        max_val = max(max_val, sum(1 if e[0] <= 0 else 0 for e in egg))
        return
    # 현재 들고있는 계란이 깨졌거나 깰 수 있는 계란이 없다면 넘어감
    if egg[start][0] <= 0 or all(egg[i][0] <= 0 for i in range(N) if i != start):
        backtrack(start + 1)
        return
    # 현재 계란으로 깨지지 않은 다른 계란을 찾아서 치는 동작 실행  
    for i in range(N):
        if i != start and egg[i][0] > 0:
            egg[start][0] -= egg[i][1]
            egg[i][0] -= egg[start][1]
            backtrack(start + 1)
            egg[start][0] += egg[i][1]
            egg[i][0] += egg[start][1]
            
        
max_val = 0    
backtrack(0)
print(max_val)