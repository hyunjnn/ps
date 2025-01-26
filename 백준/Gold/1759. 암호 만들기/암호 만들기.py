import sys
input = sys.stdin.readline

L, C = map(int, input().split())
chars = sorted(input().split())

def is_valid(password):
    vowel = consonant = 0
    for c in password:
        if c in "aeiou":
            vowel += 1 
        else:
            consonant += 1
    return vowel >= 1 and consonant >= 2
            

def backtrack(start, count, password):
    if count == L:
        if is_valid(password):
            print("".join(password))
            return
    for i in range(start, C):
        password.append(chars[i])
        backtrack(i + 1, count + 1, password)
        password.pop()

        
password = []        
backtrack(0, 0, password)
