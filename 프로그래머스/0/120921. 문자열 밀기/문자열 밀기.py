def solution(A, B):
    answer = 0
    for i in A:
        if A == B:
            break
        A = A[-1] + A[:-1]
        answer += 1
    if A != B:
        answer = -1
    return answer