a, b, v = map(int, input().split())

dist = v - b # 낮에 정상에 도달할 수 있어 v - b 까지 도달 시 정상에 도달한 것과 같음

if (v - b) % (a - b) == 0:
    days = (v - b) // (a - b)
else:
    days = (v - b) // (a - b) + 1

print(days)