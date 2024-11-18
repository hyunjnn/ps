def solution(prices):
    N = len(prices)
    answer = [0 for _ in range(N)]
    stck = []
    
    for i in range(N):
        while stck and prices[i] < prices[stck[-1]]:
            j = stck.pop()
            answer[j] = i - j
        stck.append(i)
        
    while stck:
        j = stck.pop()
        answer[j] = N - j - 1
    return answer