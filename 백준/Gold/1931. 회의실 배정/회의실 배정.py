# 회의 수 입력
N = int(input())

arr = []
for _ in range(N):
    start, end = map(int, input().split())
    arr.append((start, end))
    
# 끝나는 시간이 빠르면서 먼저 시작하는 순으로 정렬
arr.sort(key= lambda x: (x[1], x[0]))

# 끝나는 시간이 빠른 것을 선택해야 남은 시간 동안 최대한 많은 회의를 할 수 있고
end_time = arr[0][1]
count = 1

for i in range(1, N):
    # 앞 회의가 끝나는 시간보다 회의 시작 시간이 같거나 뒤인 경우
    if arr[i][0] >= end_time:
        # 회의가 가능함
        count += 1
        end_time = arr[i][1]

print(count)  # 가능한 최대 회의 수 출력