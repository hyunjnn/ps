from sys import stdin


def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    for k in range(2, int(n ** 0.5) + 1):
        if n % k == 0:
            return False
    return True


n = int(input().strip())
for _ in range(n):
    num = int(stdin.readline().strip())

    while True:
        if is_prime(num):
            print(num)
            break
        else:
            num += 1

