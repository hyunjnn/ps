arr = list(map(int, input().split()))
max_val = max(arr)
min_val = min(arr)
mid_val = sum(arr) - min_val - max_val

while True:
    if min_val + mid_val > max_val:
        break
    max_val -= 1
print(min_val + mid_val + max_val)