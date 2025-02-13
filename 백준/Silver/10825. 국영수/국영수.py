import sys
input = sys.stdin.readline

N = int(input())
students = []
for _ in range(N):
    name, *score = input().split() 
    scores = list(map(int, score))
    students.append((name, scores[0], scores[1], scores[2]))
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
    
print("\n".join(stu[0] for stu in students))