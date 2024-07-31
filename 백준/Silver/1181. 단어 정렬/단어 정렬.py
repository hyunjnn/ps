from sys import stdin

n = int(input())
arr = []
for _ in range(n):
    arr.append(stdin.readline().strip())
arr.sort(key= lambda x: (len(x), x))

for i in range(len(arr) - 1):
    if arr[i] == arr[i + 1]:
        continue
    print(arr[i])
print(arr[-1])