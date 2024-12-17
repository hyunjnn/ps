def dfs(index, arr, current_sum, target):
    if index == len(arr):
        return 1 if current_sum == target else 0
    
    return dfs(index + 1, arr, current_sum + arr[index], target) + dfs(index + 1, arr, current_sum - arr[index], target)
    

def solution(numbers, target):
    answer = dfs(0, numbers, 0, target)
    return answer