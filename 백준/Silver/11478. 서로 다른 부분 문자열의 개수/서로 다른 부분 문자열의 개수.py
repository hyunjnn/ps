s = input()
sub_set = set()
for i in range(len(s)):
    for j in range(i, len(s)):
        sub_set.add(s[i:j+1])
print(len(list(sub_set)))