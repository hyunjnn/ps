from itertools import permutations

N, M = map(int, input().split())
nums = [i for i in range(1, N + 1)]

for x in permutations(nums, M):
    print(" ".join(list(map(str, x))))