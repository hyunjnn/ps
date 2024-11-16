def solution(myString, pat):
    myString = myString.translate(str.maketrans('AB','BA'))
    
    return 1 if pat in myString else 0