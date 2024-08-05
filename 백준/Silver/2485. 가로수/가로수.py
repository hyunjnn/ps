import math

n = int(input())
arr = []
diff_arr = []
for _ in range(n):
    arr.append(int(input()))

for i in range(1, n):
    diff_arr.append(arr[i] - arr[i - 1])

GCD = math.gcd(*diff_arr)
res = 0
for k in diff_arr:
    res += k // GCD - 1
print(res)