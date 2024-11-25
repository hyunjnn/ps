from collections import deque

N = int(input())
# 자료구조 정보(0: 큐, 1: 스택)
A = list(map(int, input().split()))
# 자료구조에 들어있는 원소 값
B = list(map(int, input().split()))
# 삽입할 수열의 길이
M = int(input())
# 삽입할 원소 값
C = list(map(int, input().split()))

dq = deque()
for i in range(N):
    if A[i] == 0:
        dq.append(B[i])

for c in C:
    dq.appendleft(c)
    print(dq.pop(), end=" ")