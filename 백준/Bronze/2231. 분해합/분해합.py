n = int(input())
for k in range(1, n + 1):
    sub_sum = sum(map(int, str(k)))
    if sub_sum + k == n:
        print(k)
        break
    if k == n:
        print(0)