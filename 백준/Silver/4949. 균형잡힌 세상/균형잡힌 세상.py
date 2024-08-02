from sys import stdin

while True:
    st = stdin.readline().rstrip()
    stack = []

    if st == '.':
        break

    for s in st:
        if s == '[' or s == '(':
            stack.append(s)
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append("*")
                break
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append("*")
                break

    if stack:
        print("no")
    else:
        print("yes")

