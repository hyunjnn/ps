def solution(d, budget):
    answer = 0
    for c in sorted(d):
        if budget - int(c) >=0:
            answer+=1
            budget-=int(c)
        else:
            break
    return answer