import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    requests = []
    
    for _ in range(M):
        request = list(map(int, input().split()))
        requests.append((request[0], request[1]))
        
    sorted_requests = sorted(requests, key=lambda x: (x[1], x[0])) 
    
    used = [False] * (N + 1)
    max_students = 0
    
    for start, end in sorted_requests:
        for book in range(start, end + 1):
            if not used[book]:
                max_students += 1
                used[book] = True
                break
                
    print(max_students)