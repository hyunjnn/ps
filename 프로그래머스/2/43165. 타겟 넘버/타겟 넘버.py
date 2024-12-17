from itertools import product

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    res = list(map(sum, product(*l)))
    return res.count(target)