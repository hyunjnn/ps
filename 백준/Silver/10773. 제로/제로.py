k = int(input())
num = []
for i in range(k):
    n = int(input())
    if n == 0:
        num.pop()
    else:
        num.append(n)
print(sum(num))