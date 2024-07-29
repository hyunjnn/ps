n = int(input())
x_arr = []
y_arr = []
for i in range(n):
    x, y = map(int, input().split())
    x_arr.append(x)
    y_arr.append(y)
width = max(x_arr) - min(x_arr)
height = max(y_arr) - min(y_arr)
print(width * height)