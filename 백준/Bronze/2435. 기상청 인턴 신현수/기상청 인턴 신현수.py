import sys
N, K = map(int, input().split())
temps = list(map(int, sys.stdin.readline().split()))
max_val = -999
for i in range(N - K + 1):
    s = sum(temps[i:i+K])
    if s > max_val:
        max_val = s
print(max_val)