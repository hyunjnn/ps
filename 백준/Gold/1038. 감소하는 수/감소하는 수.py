from itertools import combinations

N = int(input())
decreasing_nums = []
for i in range(1, 11):  # 1 ~ 10자리수
    for n in combinations(range(9, -1, -1), i):  # 9부터 조합해야 감소하는 수가 됨
        decreasing_nums.append(int("".join(map(str, n))))
        
decreasing_nums.sort()
if len(decreasing_nums) <= N:
    print(-1)
else:
    print(decreasing_nums[N])