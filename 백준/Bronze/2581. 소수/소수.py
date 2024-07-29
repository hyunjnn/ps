import math

def is_prime(t):
    if t == 1:
        return False
    if t == 2: 
        return True
    for k in range(2, int(math.sqrt(i) + 1)):
        if t % k == 0:
            return False
    return True


m = int(input())
n = int(input())
prime_arr = []
for i in range(m, n + 1):
    if is_prime(i):
        prime_arr.append(i)
if len(prime_arr) == 0:
    print(-1)
else:
    print(sum(prime_arr))
    print(min(prime_arr))