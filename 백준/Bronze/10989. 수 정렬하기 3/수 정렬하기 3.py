from sys import stdin

n = int(stdin.readline())
num_arr = [0] * 10001

for _ in range(n):
    num_arr[int(stdin.readline())] += 1

for i in range(10001):
    if num_arr[i] != 0:
        for _ in range(num_arr[i]):
            print(i)