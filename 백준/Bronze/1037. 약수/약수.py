N = int(input())
nums = list(map(int, input().split()))
sorted_nums = sorted(nums)
if len(sorted_nums) < 2:
    print(sorted_nums[0] * sorted_nums[0])
else:
    print(sorted_nums[0] * sorted_nums[-1])