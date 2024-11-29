from collections import defaultdict
import sys

N, M = map(int, input().split())
words = defaultdict(int)

for _ in range(N):
    word = sys.stdin.readline().strip()
    if len(word) >= M:
        words[word] += 1
    
sorted_words = sorted(words.items(), key= lambda x: (-x[1], -len(x[0]), x[0]))
for word, _ in sorted_words:
    print(word)