from sys import stdin

NUM = 123456 * 2 + 1
is_prime = [1] * NUM
for i in range(2, NUM):
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime[i] = 0
            break

while True:
    num = int(stdin.readline().strip())
    if num == 0:
        break
        
    cnt = 0
    for k in range(num + 1, num * 2 + 1):
        cnt += is_prime[k]
    print(cnt)