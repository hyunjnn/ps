N = int(input())
names = {"ChongChong"}
count = 1
for _ in range(N):
    arr = list(input().split())
    if all(x in names for x in arr):
        continue
    if any(x in names for x in arr):
        if arr[0] in names:
            names.add(arr[1])
        else:
            names.add(arr[0])
        count += 1 
print(count)