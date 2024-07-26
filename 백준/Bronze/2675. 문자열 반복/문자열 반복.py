T = int(input())
for _ in range(T):
    rep_cnt, text = input().split()
    for i in text:
        print(i * int(rep_cnt), end='')
    print()