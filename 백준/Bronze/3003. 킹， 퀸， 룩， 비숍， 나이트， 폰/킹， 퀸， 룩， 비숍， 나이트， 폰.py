pieces_cnt = [1, 1, 2, 2, 2, 8]
white_pieces = list(map(int, input().strip().split()))

for i in range(len(pieces_cnt)):
    print(pieces_cnt[i] - white_pieces[i], end=' ')