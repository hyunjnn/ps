from collections import deque
import heapq
T = int(input())
for _ in range(T):
    
    # 문서 개수, 인쇄 순서가 궁금한 문서의 인덱스 번호
    N, M = map(int, input().split())
    # 문서의 중요도
    arr = list(map(int, input().split()))
    
    dq = deque((priority, i) for i, priority in enumerate(arr))
        
    res = 0
    while True:
        data = dq.popleft()
        if any(data[0] < x[0] for x in dq):
            dq.append(data)
        else:
            res += 1
            if data[1] == M:
                break
    print(res)
            
