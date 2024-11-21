import sys
from collections import Counter
N = int(input())
numbers = [int(sys.stdin.readline().strip()) for _ in range(N)]
               
num_counter = Counter(numbers)
res = []
max_val = num_counter.most_common(1)[0][1]
for k in num_counter.keys():
    if num_counter[k] == max_val:
        res.append(k)
print(sorted(res)[0])