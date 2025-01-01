from math import ceil

def solution(progresses, speeds):
    answer = []
    
    # 각 작업별 남은 작업 일수 계산
    tasks = [
        ceil((100 - p) / s)
        for p, s in zip(progresses, speeds)
    ]
    
    i = 0
    while i < len(tasks):
        current = tasks[i]
        cnt = 0
        
        while i < len(tasks) and tasks[i] <= current:
            i += 1
            cnt += 1
            
        answer.append(cnt)
    
    return answer