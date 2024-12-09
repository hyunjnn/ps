import sys

M = int(input())
S = set()
for _ in range(M):
    cmd = sys.stdin.readline().strip().split()
    if len(cmd) > 1:
        if cmd[0] == "add":
            S.add(int(cmd[1]))
        elif cmd[0] == "remove":
            S.discard(int(cmd[1]))
        elif cmd[0] == "check":
            print(1) if int(cmd[1]) in S else print(0)
        elif cmd[0] == "toggle":  
            S.discard(int(cmd[1])) if int(cmd[1]) in S else S.add(int(cmd[1]))
    else:
        S.clear()
        if cmd[0] == "all":
            S = {i for i in range(1, 21)}
           