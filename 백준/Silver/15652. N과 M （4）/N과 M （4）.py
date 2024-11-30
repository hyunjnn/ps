from itertools import combinations_with_replacement

N, M = map(int, input().split())
nums = [i for i in range(1, N + 1)]
for x in combinations_with_replacement(nums, M):
    print(" ".join(list(map(str, x))))