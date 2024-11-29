n = int(input())
count = 0

def fibo(n):
    global count
    if n == 1 or n == 2:
        count += 1
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

fibo(n)
print(count, n - 2)