K = int(input())
d = [(0, 0)] * (K + 1)
d[0] = (1, 0)
d[1] = (0, 1)
for i in range(2, K + 1):
    d[i] = (sum(d[i - 1]) - d[i - 1][0], sum(d[i - 1]))

print(" ".join(map(str, d[K])))