from sys import stdin

n = int(input())
stc = []
for i in range(n):
    cmd = list(map(int, stdin.readline().split()))

    if cmd[0] == 1:
        stc.append(cmd[1])
    elif cmd[0] == 2:
        print(stc.pop()) if len(stc) != 0 else print(-1)
    elif cmd[0] == 3:
        print(len(stc))
    elif cmd[0] == 4:
        print(1) if len(stc) == 0 else print(0)
    elif cmd[0] == 5:
        print(stc[-1]) if len(stc) != 0 else print(-1)