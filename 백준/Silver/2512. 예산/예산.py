# 지방의 수
N = int(input())
# 예산 요청 금액
nums = list(map(int, input().split()))
# 총 예산
M = int(input())

# 상한액 초깃값 설정
start = 0
end = max(nums)

# 상한액을 저장할 변수
res = 0

while start <= end:
    # 새로운 상한액 지정
    mid = (start + end) // 2
    # 배정한 총 예산
    total = 0
    for n in nums:
        # 요청 예산이 상한액보다 작은 경우, 그대로 배정
        if n <= mid:
            total += n
        # 요청 예산이 상한액보다 큰 경우, 상한액만큼 배정
        else:
            total += mid    
    # 배정한 예산이 총 예산을 넘지 않으면, 상한액을 늘림        
    if total <= M:
       # 상한액 기록
        res = mid
        start = mid + 1
    # 배정한 예산이 총 예산을 넘으면, 상한액 삭감
    else:
        end = mid - 1
# 상한액 출력    
print(res)    