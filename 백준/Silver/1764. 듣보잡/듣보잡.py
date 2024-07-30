n ,m = map(int, input().split())
s1 = set()
s2 = set()
for _ in range(n):
    s1.add(input())
for _ in range(m):
    s2.add(input())

total_name = sorted(list(s1.intersection(s2)))
print(len(total_name))
for name in total_name:
    print(name)