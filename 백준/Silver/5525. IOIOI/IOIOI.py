N = int(input())
M = int(input())
S = input()
pn = "IO" * N + "I"
count = 0
for i in range(len(S) - len(pn) + 1):
    sub_str = S[i:i+len(pn)]
    if sub_str == pn:
        count += 1
print(count)