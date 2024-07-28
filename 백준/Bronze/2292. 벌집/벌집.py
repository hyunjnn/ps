n = int(input())
row_max = 1
move = 1
while n > row_max:
    row_max += 6 * move
    move += 1
print(move)