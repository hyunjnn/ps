N, K = map(int, input().split())
answer = []
idx = K - 1
people = [i for i in range(1, N + 1)]
for i in range(N):
    answer.append(str(people.pop((idx))))
    if people:
        idx = (idx + K - 1) % len(people)
    
print("<", end="")
print(", ".join(answer), end="")
print(">")