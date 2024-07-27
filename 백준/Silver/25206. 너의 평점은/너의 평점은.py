total_sum = 0
sub_sum = 0
score = {
    'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0
}
# rank_arr = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
# avg_arr =[4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
for _ in range(20):
    a, b, c = input().split()
    b = float(b)
    if c != 'P':
        total_sum += b
        sub_sum += b * score.get(c)

print('%.6f' % (sub_sum / total_sum))