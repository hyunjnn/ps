from itertools import permutations

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*4, reverse=True)
    numbers = "".join(numbers)
    
    return str(int(numbers))

    