import sys

words = [list(sys.stdin.readline().strip())
         for _ in range(5)]

for i in range(max(len(t) for t in words)):
    for j in range(5):
        if i < len(words[j]):
            print(words[j][i], end='')