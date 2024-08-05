from sys import stdin

stack = []
n = int(input())
arr = list(map(int, stdin.readline().split()))

cnt = 1
for i in range(n):
    stack.append(arr[i])

    while stack and stack[-1] == cnt:
        stack.pop()
        cnt += 1

if stack:
    print("Sad")
else:
    print("Nice")