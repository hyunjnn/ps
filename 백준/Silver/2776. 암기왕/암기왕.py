T = int(input())
for _ in range(T):
    N = int(input())
    note1 = set(list(map(int, input().split())))
    M = int(input())
    note2 = list(map(int, input().split()))
    for x in note2:
        print(1) if x in note1 else print(0)