import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N, M = map(int, input().split())
    data = [map(int, input().split()) for _ in range(M)]
    print(N-1)