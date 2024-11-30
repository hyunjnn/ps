from itertools import combinations

N, K = map(int, input().split())
print(len(list(combinations([i for i in range(1, N + 1)], K))))