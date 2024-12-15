import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville:
        first = heapq.heappop(scoville)
        if first >= K:
            return answer
        if not scoville:
            return -1
        second = heapq.heappop(scoville)
        new_scoville = first + second * 2
        heapq.heappush(scoville, new_scoville)
        answer += 1
    
    
    