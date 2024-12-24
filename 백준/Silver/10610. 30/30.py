N = list(input())
N.sort(key=lambda x: x*5, reverse=True)
if int("".join(N)) % 30 == 0:
    print(int("".join(N)))
else:
    print(-1)