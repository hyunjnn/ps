import sys
input = sys.stdin.readline

for _ in range(int(input())):
    data = input()
    score = 0
    total = 0
    for d in data:
        if d == "O":
            score += 1 
        else:
            score = 0
        total += score
                       
    print(total)