# 에라토스테네스의 체 알고리즘 사용
prime_num = [1 for _ in range(1000001)]
for i in range(2, 1000001):
    if prime_num[i]:
        for j in range(2 * i, 1000001, i):
            prime_num[j] = 0

t = int(input())

for _ in range(t):
    n = int(input())
    res = 0
    # 절반 이상의 범위 부터는 두 값의 순서만 바뀌기 때문에 검사할 필요 없음
    for j in range(2, n // 2 + 1):
        # 두 수의 합이 n 이면서 각각의 값이 소수일 때 카운트 증가
        if prime_num[j] and prime_num[n - j]:
            res += 1
    print(res)
