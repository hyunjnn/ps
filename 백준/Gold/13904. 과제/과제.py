N = int(input())
tasks = []
for _ in range(N):
    deadline, score = map(int, input().split())
    tasks.append((deadline, score))
    
# 점수가 높은 순으로 정렬
tasks.sort(key = lambda x: -x[1])

# 마감일 배정 여부
days = [False] * 1001

max_score = 0
for deadline, score in tasks:
    for i in range(deadline, 0, -1):
        if not days[i]:
            max_score += score
            days[i] = True
            break
    
print(max_score)