def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

N = int(input())
num_arr = list(map(int, input().split()))
cnt = 0
for k in num_arr:
    if is_prime(k):
        cnt += 1
print(cnt)