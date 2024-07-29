x_arr = []
x3 = 0
y_arr = []
y3 = 0
for i in range(3):
    x, y = map(int, input().split())
    if x not in x_arr:
        x_arr.append(x)
    else:
        x3 = x
    if y not in y_arr:
        y_arr.append(y)
    else:
        y3 = y
print(sum(x_arr) - x3, sum(y_arr) - y3)