N, K = map(int, input().split())
nums = list(map(int, input().split()))

# 구간합
window = sum(nums[:K])
res = window

for i in range(K, N):
    # 구간합 다음 수 더하고 맨 앞의 수 빼기
    window += (nums[i] - (nums[i - K]))
    # 구간합 최대값 기록
    res = max(res, window)
    
# 구간합 최대값 출력
print(res)