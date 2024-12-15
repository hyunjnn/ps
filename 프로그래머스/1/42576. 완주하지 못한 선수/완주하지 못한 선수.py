from collections import Counter

def solution(participant, completion):
    answer = ''
    c1 = Counter(participant)
    c2 = Counter(completion)
    for name in set(participant):
        if c1[name] != c2[name]:
            answer += name
    return answer