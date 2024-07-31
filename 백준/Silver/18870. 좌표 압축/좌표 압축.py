from sys import stdin

n = int(input())
x_arr = list(map(int, stdin.readline().split()))
x_set = sorted(set(x_arr))
cnt_dict = {x_set[i] : i for i in range(len(x_set))}

for k in x_arr:
    print(cnt_dict[k], end=' ')