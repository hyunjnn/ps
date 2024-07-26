N = int(input())
group_word_cnt = N

for i in range(N):
    word = input()
    for j in range(len(word) - 1):
        if word[j] == word[j + 1]:
            continue
        elif word[j] in word[j + 1:]:
            group_word_cnt -= 1
            break
print(group_word_cnt)