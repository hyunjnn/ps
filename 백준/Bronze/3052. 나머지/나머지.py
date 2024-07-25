arr = []
for _ in range(10):
    tmp = int(input()) % 42
    if tmp not in arr:
        arr.append(tmp)

print(len(arr))