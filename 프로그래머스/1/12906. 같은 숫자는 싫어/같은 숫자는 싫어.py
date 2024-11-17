def solution(arr):
    stck = []
    for i in arr:
        if stck and stck[-1] == i:
            continue
        else:
            stck.append(i)
    return stck