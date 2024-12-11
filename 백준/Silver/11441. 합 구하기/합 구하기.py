N = int(input())
nums = list(map(int, input().split()))

s = 0 
sum_arr = [0]
for n in nums:
    s += n 
    sum_arr.append(s)
M = int(input())
for _ in range(M):
    i, j = map(int, input().split())
    print(sum_arr[j] - sum_arr[i-1])