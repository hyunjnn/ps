from heapq import heappush, heappop

# 테스트 케이스 개수
T = int(input())
for _ in range(T):
    min_heap = []
    max_heap = []
    valid = {}  # 숫자 카운트
    
    # 적용할 연산의 개수
    k = int(input())
    for _ in range(k):
        cmd, n = input().split()
        n = int(n)
        
        if cmd[0] == "I":  # 삽입 연산
            heappush(min_heap, n)
            heappush(max_heap, -n)
            # 해당 숫자 카운트 증가
            valid[n] = valid.get(n, 0) + 1
            
        elif cmd[0] == "D":  # 삭제 연산
            if n == -1:  # 최솟값 삭제
                while min_heap and valid.get(min_heap[0], 0) == 0:
                    heappop(min_heap)
                if min_heap:
                    data = heappop(min_heap)
                    valid[data] -= 1
            elif n == 1:  # 최댓값 삭제
                while max_heap and valid.get(-max_heap[0], 0) == 0:
                    heappop(max_heap)
                if max_heap:
                    data = -heappop(max_heap)
                    valid[data] -= 1
    
    while min_heap and valid.get(min_heap[0], 0) == 0:
        heappop(min_heap)
    while max_heap and valid.get(-max_heap[0], 0) == 0:
        heappop(max_heap)
    
    # 최대, 최솟값 출력
    if min_heap and max_heap:
        print(-max_heap[0], min_heap[0])
    else:
        print("EMPTY")