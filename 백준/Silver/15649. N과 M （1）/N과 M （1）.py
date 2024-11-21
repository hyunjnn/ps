from itertools import permutations

N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
for x in permutations(arr, M):
    print(" ".join(list(map(str, x))))