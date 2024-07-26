word = input()
total_time = 0

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
for i in range(len(word)):
    for j in range(len(dial)):
        if word[i] in dial[j]:
            total_time += j + 3

print(total_time)