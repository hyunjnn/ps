def solution(s):
    stck = []
    for i in s:
        if i == "(":
            stck.append(i)
        else:
            if stck and stck[-1] == "(":
                stck.pop()
            else:
                return False
    return False if stck else True