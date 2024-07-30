a, b = map(int, input().split())
s1 = set(list(map(int, input().split())))
s2 = set(list(map(int, input().split())))

print(len(list(s1 - s2)) + len(list(s2 - s1)))