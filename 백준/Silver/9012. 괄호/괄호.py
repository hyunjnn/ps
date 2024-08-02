n = int(input())
for i in range(n):
    stc = []
    vs = input()

    for s in vs:
        if s == '(':
            stc.append(s)
        elif s == ')':
            if stc:
                stc.pop()
            else:
                print("NO")
                break
    else:
        if stc:
                print("NO")            
        else:
            print("YES")