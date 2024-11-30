from collections import defaultdict

N = int(input())
arr = []
counter = defaultdict(int)
for _ in range(N):
    n = int(input())
    arr.append(n)
    counter[n] += 1

# 산술 평균
print(round(sum(arr) / N))

# 중앙값
sorted_arr = sorted(arr)
print(sorted_arr[N // 2])

# 최빈값
sorted_counter = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
if len(sorted_counter) > 1 and sorted_counter[0][1] == sorted_counter[1][1]:
        print(sorted_counter[1][0])
else:
    print(sorted_counter[0][0])

# 범위
print(max(arr) - min(arr))    