def is_palindrom(num):
    N = len(num)
    for i in range(N // 2):
        if num[i] != num[N - i - 1]:
            return "no"
    return "yes"

while True:
    n = input()
    if n == '0':
        break
    print(is_palindrom(n))
    
        