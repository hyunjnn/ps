import sys
data = sys.stdin.read().splitlines()

N, X = map(int, data[0].split())
nums = list(map(int, data[1].split()))

window = sum(nums[:X])
count = 1
max_val = window

for i in range(X, N):
    window -= nums[i-X]
    window += nums[i]
    if window == max_val:
        count += 1
    elif window > max_val:
        max_val = window
        count = 1

if max_val == 0:
    print("SAD")
else:
    print(max_val)
    print(count)