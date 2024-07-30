from itertools  import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))
res = 0
for k in combinations(cards, 3):
    tmp = sum(k)
    if res < tmp <= m:
        res = tmp

print(res)