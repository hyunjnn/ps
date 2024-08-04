from itertools import combinations

prime_num = [1 for _ in range(1000001)]
for i in range(2, 1000001):
    if prime_num[i]:
        for j in range(2 * i, 1000001, i):
            prime_num[j] = 0

t = int(input())


for i in range(t):
    n = int(input())
    res = 0
    for j in range(2, n // 2 + 1):
        if prime_num[j] and prime_num[n - j]:
            res += 1
    print(res)



