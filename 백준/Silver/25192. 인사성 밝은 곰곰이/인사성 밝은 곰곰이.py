N = int(input())
names = set()
count = 0
for _ in range(N):
    log = input()
    if log == "ENTER":
        names = set()
    elif log not in names:
        names.add(log)
        count += 1
print(count)