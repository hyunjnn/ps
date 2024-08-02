from sys import stdin
from collections import deque

n = int(input())
queue = deque()

for i in range(n):
    cmd = list(map(int, stdin.readline().split()))

    if cmd[0] == 1:
        queue.appendleft(int(cmd[1]))
    elif cmd[0] == 2:
        queue.append(int(cmd[1]))
    elif cmd[0] == 3:
        print(queue.popleft()) if queue else print(-1)
    elif cmd[0] == 4:
        print(queue.pop()) if queue else print(-1)
    elif cmd[0] == 5:
        print(len(queue)) 
    elif cmd[0] == 6:
        print(1) if not queue else print(0)
    elif cmd[0] == 7:
        print(queue[0]) if queue else print(-1)
    elif cmd[0] == 8:
        print(queue[-1]) if queue else print(-1)
