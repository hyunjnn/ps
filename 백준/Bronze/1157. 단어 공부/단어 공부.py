word = list(input().upper())
alpha_cnt_list = [0] * 26

for i in word:
    alpha_cnt_list[ord(i) - 65] += 1
if alpha_cnt_list.count(max(alpha_cnt_list)) >= 2:
    print("?")
else:
    print(chr(alpha_cnt_list.index(max(alpha_cnt_list)) + 65))
# print(*alphabet_cnt)