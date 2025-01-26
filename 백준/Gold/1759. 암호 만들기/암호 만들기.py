import sys
from itertools import combinations
input = sys.stdin.readline

def is_valid(password):
    vowel = sum(1 if p in "aeiou" else 0 for p in password)
    consonant = len(password) - vowel
    return vowel >= 1 and consonant >= 2


L, C = map(int, input().split())

for password in combinations(sorted(input().split()), L):
    if is_valid(password):
        print("".join(password))