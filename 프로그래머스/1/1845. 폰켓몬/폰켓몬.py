def solution(nums):
    unique_mon = len(set(nums))
    max_mon = len(nums) // 2
    return min(unique_mon, max_mon)