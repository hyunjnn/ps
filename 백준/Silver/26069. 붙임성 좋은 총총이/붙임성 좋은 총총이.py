N = int(input())
names = {"ChongChong"}
for _ in range(N):
    a, b = input().split()
    if a in names or b in names:
        names.add(a)
        names.add(b)
print(len(names))