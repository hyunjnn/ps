import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

for n in permutations(sorted(nums), M):
    print(" ".join(map(str, n)))