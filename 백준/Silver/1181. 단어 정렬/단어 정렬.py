from sys import stdin

n = int(input())
arr = []
for _ in range(n):
    arr.append(stdin.readline().strip())

num_set = set(arr)
num_arr = list(num_set)
num_arr.sort(key= lambda x: (len(x), x))

for i in num_arr:
    print(i)
