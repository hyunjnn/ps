from itertools import permutations

N, M = map(int, input().split())
nums = [i for i in range(1, N + 1)]

res = permutations(nums, M)
for x in res:
    print(str(x).replace("(", "").replace(")", "").replace(",", ""))