n = int(input())
lectures = []
for _ in range(n):
    pay, deadline = map(int, input().split())
    lectures.append((pay, deadline))

# 강연료가 비싼 순으로 정렬
lectures.sort(key=lambda x: -x[0])

# 강연 날짜 배정 여부
scheduled = [False] * 10001

money = 0
for pay, deadline in lectures:
    # 최대한 늦은 날짜에 배정해야 강연 횟수가 늘어남
    for day in range(deadline, 0, -1):
        if not scheduled[day]:
            scheduled[day] = True
            money += pay
            break

print(money)