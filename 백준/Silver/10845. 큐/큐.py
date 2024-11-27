from collections import deque

N = int(input())
q = deque()
for _ in range(N):
    cmd = input().split()
    if len(cmd) > 1:
        if cmd[0] == "push":
            q.append(int(cmd[1]))
    else:
        if cmd[0] == "pop":
            print(q.popleft()) if q else print(-1)
        elif cmd[0] == "size":
            print(len(q))
        elif cmd[0] == "empty":
            print(1) if not q else print(0)
        elif cmd[0] == "front":
            print(q[0]) if q else print(-1)
        elif cmd[0] == "back":
            print(q[-1]) if q else print(-1)
    