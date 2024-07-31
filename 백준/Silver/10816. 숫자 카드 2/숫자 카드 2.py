from sys import stdin

n = int(input())
card_num = list(map(int,stdin.readline().split()))

m = int(input())
check_num = list(map(int, stdin.readline().split()))

# 카드 숫자를 키로 하고, 숫자 개수를 값으로 하는 딕셔너리 생성
cnt_dict = {}
for i in card_num:
    if i in cnt_dict:
        cnt_dict[i] += 1
    else:
        cnt_dict[i] = 1

for k in check_num:
    if cnt_dict.get(k) == None:
        print(0, end=' ')
    else:
        print(cnt_dict.get(k), end=' ')