import sys
from collections import deque
input = sys.stdin.readline

def is_matching(cow):
    for barn in preferredBarns[cow]:
        if not visited[barn]: 
            visited[barn] = True
            if matched[barn] == 0 or is_matching(matched[barn]):
                matched[barn] = cow
                return True
    return False
                
    
COW, BARN = map(int, input().split())
preferredBarns = [[] for _ in range(COW + 1)]
for cow in range(1, COW + 1):
    _, *barns = input().split()
    preferredBarns[cow].extend(map(int, barns))
matched = {barn: 0 for barn in range(1, BARN + 1)}
    
res = 0
for cow in range(1, COW + 1):
    visited = [False] * (BARN + 1)
    if is_matching(cow):
        res += 1
print(res)