def solution(myString, pat):
    myString = myString.upper()
    pat = pat.upper()
    
    return 1 if pat in myString else 0