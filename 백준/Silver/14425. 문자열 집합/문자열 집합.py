from sys import stdin

n, m = map(int, input().split())
origin_set = set([stdin.readline().strip()
               for _ in range(n)])

check_str = [stdin.readline().strip()
               for _ in range(m)]

cnt = 0
for s in check_str:
    if {s} - origin_set == set():
        cnt += 1

print(cnt)