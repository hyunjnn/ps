n = int(input())
people_set = set()

for _ in range(n):
    name, state = input().split()

    if state == 'enter':
        people_set.add(name)
    elif state == 'leave':
        people_set.remove(name)

for p in sorted(list(people_set), reverse=True):
    print(p)