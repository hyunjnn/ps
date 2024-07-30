import math

def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

m, n = map(int, input().split())
prime_num = []
for k in range(m, n + 1):
    if is_prime(k):
        prime_num.append(k)
prime_num.sort()
for j in prime_num:
    print(j)